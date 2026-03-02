#pequeño script python que procesan los .md antes de ser renderizados a HTML
import re
def on_page_markdown(markdown, **kwargs):
    pattern = r'\s*\$\$(.*?)\$\$\s*'
    corrected_markdown = re.sub(
        pattern, 
        r'\n\n$$\1$$\n\n', 
        markdown, 
        flags=re.DOTALL
    )
    return corrected_markdown