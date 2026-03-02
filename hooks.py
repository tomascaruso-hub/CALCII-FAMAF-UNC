import re
import os

file_map = {}

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

def on_page_markdown(markdown, page, config, files):
    # buscamos bloques $$ y aseguramos el salto de línea \n\n
    pattern_latex = r'\s*\$\$(.*?)\$\$\s*'
    markdown = re.sub(pattern_latex, r'\n\n$$\1$$\n\n', markdown, flags=re.DOTALL)

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