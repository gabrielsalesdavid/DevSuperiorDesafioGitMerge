from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from pathlib import Path
import datetime

# Configurações
output_path = Path(__file__).parent / "README_COMPLETO.pdf"
readme_path = Path(__file__).parent / "README_COMPLETO.md"

# Ler conteúdo markdown
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Criar documento PDF
doc = SimpleDocTemplate(str(output_path), pagesize=A4, topMargin=0.5*inch, bottomMargin=0.5*inch)

# Estilos
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name='CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#0066cc'),
    spaceAfter=30,
    alignment=TA_CENTER,
    borderPadding=10,
    borderColor=colors.HexColor('#0066cc'),
    borderWidth=2,
    borderRadius=5
))

styles.add(ParagraphStyle(
    name='CustomHeading',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=colors.HexColor('#0066cc'),
    spaceAfter=12,
    spaceBefore=12,
    leftIndent=0,
    borderPadding=5,
    borderColor=colors.HexColor('#0066cc'),
    borderWidth=1,
))

styles.add(ParagraphStyle(
    name='CustomBody',
    parent=styles['Normal'],
    fontSize=10,
    alignment=TA_JUSTIFY,
    spaceAfter=12
))

# Conteúdo
story = []

# Título
story.append(Paragraph("DevSuperior - Desafio Git Merge", styles['CustomTitle']))
story.append(Spacer(1, 0.2*inch))

# Descrição
description = "<b>Documentação Completa</b><br/>Guia de Versionamento com Git e GitHub"
story.append(Paragraph(description, styles['CustomBody']))
story.append(Spacer(1, 0.1*inch))

# Data
date_str = f"<i>Gerado em: {datetime.datetime.now().strftime('%d de %B de %Y às %H:%M')}</i>"
story.append(Paragraph(date_str, styles['Normal']))
story.append(Spacer(1, 0.3*inch))

# Índice
story.append(Paragraph("📋 Conteúdo", styles['Heading2']))
story.append(Paragraph("• Descrição do Projeto", styles['Normal']))
story.append(Paragraph("• Estrutura do Repositório", styles['Normal']))
story.append(Paragraph("• Como Começar", styles['Normal']))
story.append(Paragraph("• Fluxo de Trabalho Git", styles['Normal']))
story.append(Paragraph("• Gerenciamento de Branches", styles['Normal']))
story.append(Spacer(1, 0.2*inch))

# Quebra de página
story.append(PageBreak())

# Conteúdo principal
story.append(Paragraph("Conteúdo Completo do README", styles['Heading1']))
story.append(Spacer(1, 0.1*inch))

# Adicionar conteúdo do README formatado
lines = content.split('\n')
for line in lines:
    if line.startswith('# '):
        story.append(Paragraph(line[2:], styles['CustomTitle']))
        story.append(Spacer(1, 0.1*inch))
    elif line.startswith('## '):
        story.append(Paragraph(line[3:], styles['CustomHeading']))
        story.append(Spacer(1, 0.05*inch))
    elif line.startswith('### '):
        story.append(Paragraph(line[4:], styles['Heading3']))
    elif line.startswith('- '):
        story.append(Paragraph("• " + line[2:], styles['CustomBody']))
    elif line.startswith('```'):
        continue
    elif line.strip():
        # Remover markdown de formatação - convertendo para HTML correto
        line = line.replace('**', '<b>')
        line = line.replace('__', '<b>')
        # Contar **/ para fechar tags corretamente
        line = line.replace('</b></b>', '</b>')
        line = line.replace('*', '<i>')
        line = line.replace('_', '<i>')
        # Corrigir tags desbalanceadas
        import re
        # Fechar tags abertas
        if line.count('<b>') > line.count('</b>'):
            line += '</b>' * (line.count('<b>') - line.count('</b>'))
        if line.count('<i>') > line.count('</i>'):
            line += '</i>' * (line.count('<i>') - line.count('</i>'))
        try:
            story.append(Paragraph(line, styles['CustomBody']))
        except:
            # Se ainda houver erro, adicionar sem formatação
            story.append(Paragraph(line.replace('<b>', '').replace('</b>', '').replace('<i>', '').replace('</i>', ''), styles['CustomBody']))
    else:
        story.append(Spacer(1, 0.05*inch))

# Rodapé
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("___", styles['Normal']))
story.append(Spacer(1, 0.1*inch))
footer = "DevSuperior - Fundação de Programação | Git e GitHub | 2025"
story.append(Paragraph(footer, styles['Normal']))

# Gerar PDF
try:
    doc.build(story)
    print(f"✓ PDF gerado com sucesso: {output_path}")
except Exception as e:
    print(f"✗ Erro ao gerar PDF: {e}")
