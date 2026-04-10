import re
import os
import yaml 

file_map = {}
# extensiones de imagen soportadas
image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')

def on_config(config):
    file_map.clear()
    docs_dir = config['docs_dir']
    
    # escaneo de todo el repo para los links de Obsidian
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                name = file[:-3] # quitamos el .md para el índice
                file_map[name] = os.path.join(root, file)
            elif file.lower().endswith(image_extensions):
                file_map[file] = os.path.join(root, file)

    # configuración base 
    decap_config = {
        'local_backend': False,
        'locale': 'es',
        'backend': {
            'name': 'github',
            'repo': 'tomasccc/CALCII-FAMAF-UNC',
            'branch': 'main',
            'base_url': 'https://decap-proxy.tomycaruso.workers.dev',
            'open_authoring': True,
        },
        'publish_mode': 'editorial_workflow',
        'media_folder': 'docs/assets/comunidad',
        'public_folder': '/assets/comunidad',
        'collections': [] # lo llenamos con las carpetas que encontremos en comunidad/ y oficial/
    }
    collections_names = set() # para evitar duplicados en caso de nombres repetidos

    # funcion para escanear y agregar colecciones dinámicamente
    def scan_and_add_collections(base_folder_name, label_prefix):
        base_dir = os.path.join(docs_dir, base_folder_name)
        raiz_collection_name = f"{base_folder_name}_raiz"
        collections_names.add(raiz_collection_name) # agregamos la colección raíz al set para evitar duplicados
        # agregamos raiz para los archivos sueltos Y crear carpetas
        decap_config['collections'].append({
            'name': f"{base_folder_name}_raiz",
            'label': f"📂 {label_prefix} (Raíz / Crear Carpeta)",
            'folder': f"docs/{base_folder_name}",
            'path': '{{carpeta}}/{{slug}}', 
            'create': True,
            'extension': 'md',
            'summary': '{{title}}',
            'fields': [
                {
                    'label': '📁 Destino del apunte', 
                    'name': 'carpeta', 
                    'widget': 'string', 
                    'default': 'general', 
                    'required': True,
                    'hint': f'👉 Para archivo suelto: dejá la palabra "general".\n👉 Para una nueva carpeta: borrá "general" y escribí el nombre SIN ESPACIOS (ej: unidad-4).',
                    'pattern': ['^[a-zA-Z0-9_-]+$', '⚠️ El nombre no puede tener espacios, puntos ni barras. Usá guiones (ejemplo: apuntes-extra).']
                },
                {'label': 'Título', 'name': 'title', 'widget': 'string',
                 'hint': 'El título de la nota.'},
                {'label': 'Cuerpo', 'name': 'body', 'widget': 'markdown'},
                 {
                            'label': 'Autoría y Responsabilidad (Obligatorio)',
                            'name': 'check_autoria_responsabilidad',
                            'widget': 'select',
                            'options': [
                                'No estoy de acuerdo',
                                'Acepto'
                            ],
                            'default': 'No estoy de acuerdo',
                            'hint': '👉 Desplegá el menú y seleccioná "Acepto..." para habilitar el guardado.',
                            'pattern': ['Acepto', ' Debes abrir el menú desplegable y aceptar las condiciones de uso y distribución para publicar/editar.']
                        },
            ]
        })

        #  subcarpetas 
        if os.path.exists(base_dir):
            for folder_name in sorted(os.listdir(base_dir)):
                folder_path = os.path.join(base_dir, folder_name)
                
                # ignorando 'assets' o '. noseque'
                if os.path.isdir(folder_path) and not folder_name.startswith('.') and folder_name.lower() != 'assets':
                    
                    # generamos ID interno para Decap que no le gustan los espacios
                    col_id = f"{base_folder_name}_{re.sub(r'[^a-zA-Z0-9]', '_', folder_name).lower()}"

                    original_col_id = col_id
                    count = 2
                    while col_id in collections_names: # si ya existe, le agregamos un sufijo numérico
                        col_id = f"{original_col_id}_{count}"
                        count += 1
                        
                    collections_names.add(col_id) # registramos el ID final
                    # añadimos la subcarpeta 
                    decap_config['collections'].append({
                        'name': col_id,
                        'label': f"📚 {label_prefix}: {folder_name}",
                        'folder': f"docs/{base_folder_name}/{folder_name}",
                        'create': True,
                        'extension': 'md',
                        'summary': '{{title}}',
                        'fields': [
                            {'label': 'Título', 'name': 'title', 'widget': 'string'},
                            {'label': 'Cuerpo', 'name': 'body', 'widget': 'markdown'},
                            {
                            'label': 'Autoría y Responsabilidad (Obligatorio)',
                            'name': 'check_autoria_responsabilidad',
                            'widget': 'select',
                            'options': [
                                'No estoy de acuerdo',
                                'Acepto'
                            ],
                            'default': 'No estoy de acuerdo',
                            'hint': '👉 Desplegá el menú y seleccioná "Acepto..." para habilitar el guardado.',
                            'pattern': ['Acepto', ' Debes abrir el menú desplegable y aceptar las condiciones de uso y distribución para publicar/editar.']
                        },
                        ]
                    })

    # aplicamos a las carpetas
    scan_and_add_collections('comunidad', 'Comunidad')
    scan_and_add_collections('oficial', 'Oficial')

    # escribimos el config.yml
    admin_dir = os.path.join(docs_dir, 'admin')
    os.makedirs(admin_dir, exist_ok=True) 
    config_output_path = os.path.join(admin_dir, 'config.yml')

    # nuevo YAML en la memoria (como texto)
    new_yaml = yaml.dump(decap_config, allow_unicode=True, sort_keys=False)
    
    rewrite = True
    # si el archivo ya existe y qué dice adentro
    if os.path.exists(config_output_path):
        with open(config_output_path, 'r', encoding='utf-8') as f:
            yaml_existing = f.read()
        # si el yaml existente es igual al nuevo, no reescribimos     
        if new_yaml == yaml_existing:
            rewrite = False
            
    # tocamos el disco duro si hubo un cambio real como una carpeta nueva
    if rewrite:
        with open(config_output_path, 'w', encoding='utf-8') as f:
            f.write(new_yaml)


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