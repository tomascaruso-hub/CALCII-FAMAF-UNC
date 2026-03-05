import re
import os

file_map = {}
# extensiones de imagen soportadas
image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')

def on_config(config):
    file_map.clear()
    docs_dir = config['docs_dir']
    # escaneo de todo el repo
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                name = file[:-3] # quitamos el .md para el índice
                # se guarda la ruta
                file_map[name] = os.path.join(root, file)
            # indexa archivos de imagen usando su nombre completo
            elif file.lower().endswith(image_extensions):
                file_map[file] = os.path.join(root, file)

def on_page_markdown(markdown, page, config, files):
    if not markdown.strip().startswith('# '):
        # tomamos el nombre del archivo 
        title = page.title if page.title else os.path.basename(page.file.src_path).replace('.md', '')
        markdown = f"# {title}\n\n{markdown}"
    # buscamos bloques $$ y aseguramos el salto de línea \n\n
    pattern_latex = r'\s*\$\$(.*?)\$\$\s*'
    markdown = re.sub(pattern_latex, r'\n\n$$\1$$\n\n', markdown, flags=re.DOTALL)

    # funcionalidad para procesar imágenes ![[imagen.png]] o ![[imagen.png|Texto alternativo]]
    def replace_image(match):
        content = match.group(1).split('|') 
        img_name = content[0].strip()
        
        if img_name in file_map:
            target_path = file_map[img_name]
            current_dir = os.path.dirname(page.file.abs_src_path)
            rel_link = os.path.relpath(target_path, current_dir)
            return f'\n\n![{img_name}]({rel_link})\n\n'
        return f'\n\n*Imagen no encontrada: {img_name}*\n\n'

    markdown = re.sub(r'!\[\[(.*?)\]\]', replace_image, markdown)

    # corrección de hipervínculos
    def replace_link(match):
        link_content = match.group(1)
        parts = link_content.split('|')
        file_name = parts[0].strip()
        display_text = parts[1].strip() if len(parts) > 1 else file_name
        
        if file_name in file_map:
            target_path = file_map[file_name]
            current_file_dir = os.path.dirname(page.file.abs_src_path)
            rel_link = os.path.relpath(target_path, current_file_dir)
            return f'[{display_text}]({rel_link})'
        
        return f'**{display_text}**' # si no existe, queda en negrita

    pattern_links = r'\[\[(.*?)\]\]'
    markdown = re.sub(pattern_links, replace_link, markdown)

    return markdown