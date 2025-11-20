import os
import sys
from pathlib import Path

# Caminho do diretório
current_dir = Path(__file__).parent
readme_md = current_dir / "README_COMPLETO.md"
readme_html = current_dir / "README_COMPLETO.html"

# Ler markdown
with open(readme_md, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Criar HTML com estilos CSS
html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevSuperior - Desafio Git Merge</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        main {{
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        h1 {{
            color: #0066cc;
            border-bottom: 3px solid #0066cc;
            padding-bottom: 15px;
            margin-bottom: 20px;
            font-size: 2.2em;
        }}
        
        h2 {{
            color: #0066cc;
            margin-top: 30px;
            margin-bottom: 15px;
            font-size: 1.6em;
            border-left: 4px solid #0066cc;
            padding-left: 10px;
        }}
        
        h3 {{
            color: #333;
            margin-top: 20px;
            margin-bottom: 10px;
        }}
        
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            color: #d63384;
        }}
        
        pre {{
            background: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #0066cc;
            overflow-x: auto;
            margin: 15px 0;
        }}
        
        pre code {{
            color: #333;
            background: none;
            padding: 0;
        }}
        
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        
        th {{
            background: #0066cc;
            color: white;
            padding: 12px;
            text-align: left;
        }}
        
        td {{
            border: 1px solid #ddd;
            padding: 10px;
        }}
        
        tr:nth-child(even) {{
            background: #f9f9f9;
        }}
        
        ul, ol {{
            margin-left: 30px;
            margin-bottom: 15px;
        }}
        
        li {{
            margin-bottom: 8px;
        }}
        
        a {{
            color: #0066cc;
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        strong {{
            color: #0066cc;
        }}
        
        blockquote {{
            border-left: 4px solid #0066cc;
            padding-left: 15px;
            margin: 20px 0;
            color: #666;
        }}
        
        hr {{
            border: none;
            border-top: 2px solid #0066cc;
            margin: 30px 0;
        }}
    </style>
</head>
<body>
    <main>
        <section id="readme">{md_content}</section>
    </main>
</body>
</html>
"""

# Salvar HTML
with open(readme_html, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Arquivo HTML gerado: {readme_html}")

# Tentar usar weasyprint para PDF
try:
    from weasyprint import HTML
    pdf_path = current_dir / "README_COMPLETO.pdf"
    HTML(string=html).write_pdf(pdf_path)
    print(f"✓ Arquivo PDF gerado: {pdf_path}")
except ImportError:
    print("✓ Para gerar PDF, instale weasyprint: pip install weasyprint")
    print(f"✓ Você pode abrir o HTML no navegador e imprimir como PDF")
