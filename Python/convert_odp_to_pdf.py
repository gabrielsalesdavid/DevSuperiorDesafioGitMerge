#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para converter arquivo ODP para PDF
Usa LibreOffice via COM ou linha de comando
"""

import os
import subprocess
import sys
from pathlib import Path

def convert_with_libreoffice_cli(input_file, output_dir):
    """Tenta converter usando LibreOffice via linha de comando"""
    try:
        # Tenta caminhos comuns do LibreOffice no Windows
        libreoffice_paths = [
            r"C:\Program Files\LibreOffice\program\soffice.exe",
            r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
            r"C:\Program Files\LibreOffice\soffice.exe",
        ]
        
        soffice = None
        for path in libreoffice_paths:
            if os.path.exists(path):
                soffice = path
                break
        
        if not soffice:
            return False
        
        # Executar conversão
        cmd = [
            soffice,
            "--headless",
            "--convert-to", "pdf",
            "--outdir", str(output_dir),
            str(input_file)
        ]
        
        print(f"🔄 Convertendo com LibreOffice...")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print("✅ Arquivo convertido com sucesso!")
            return True
        else:
            print(f"⚠️  Erro: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("⏱️  Timeout na conversão")
        return False
    except Exception as e:
        print(f"⚠️  Erro: {e}")
        return False

def create_pdf_with_reportlab(input_file, output_dir):
    """Cria um PDF informativo como alternativa"""
    try:
        from reportlab.lib.pagesizes import letter, A4
        from reportlab.lib import colors
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
        from reportlab.lib.units import inch
        from datetime import datetime
        
        output_file = Path(output_dir) / (Path(input_file).stem + ".pdf")
        
        print(f"📝 Criando PDF informativo: {output_file}")
        
        # Criar documento
        doc = SimpleDocTemplate(str(output_file), pagesize=A4)
        story = []
        styles = getSampleStyleSheet()
        
        # Estilos customizados
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#0066cc'),
            spaceAfter=30,
            alignment=1  # Centro
        )
        
        # Conteúdo
        story.append(Paragraph("Git - Comandos e Merge com Conflito", title_style))
        story.append(Spacer(1, 12))
        
        content_style = styles['BodyText']
        
        story.append(Paragraph("📌 Informações do Arquivo", styles['Heading2']))
        story.append(Spacer(1, 8))
        
        # Tabela com informações
        info_data = [
            ["Campo", "Valor"],
            ["Arquivo Original", Path(input_file).name],
            ["Formato Original", "ODP (OpenDocument Presentation)"],
            ["Data de Geração", datetime.now().strftime("%d/%m/%Y %H:%M:%S")],
            ["Tipo de Conversão", "Informativa"],
        ]
        
        info_table = Table(info_data, colWidths=[2.5*inch, 4*inch])
        info_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0066cc')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        
        story.append(info_table)
        story.append(Spacer(1, 20))
        
        # Instruções
        story.append(Paragraph("📋 Como Converter o Arquivo Original para PDF", styles['Heading2']))
        story.append(Spacer(1, 8))
        
        instructions = [
            "1. <b>Instalar LibreOffice</b>: Baixe em https://www.libreoffice.org/",
            "2. <b>Método 1 - Via Script Python</b>: Execute o script <i>convert_odp_to_pdf.py</i>",
            "3. <b>Método 2 - Manualmente</b>: Abra o arquivo ODP no LibreOffice e exporte como PDF",
            "4. <b>Método 3 - LibreOffice CLI</b>: Use o comando abaixo no terminal",
        ]
        
        for instr in instructions:
            story.append(Paragraph(instr, content_style))
            story.append(Spacer(1, 6))
        
        story.append(Spacer(1, 12))
        story.append(Paragraph("Comando LibreOffice CLI:", styles['Heading3']))
        story.append(Spacer(1, 6))
        
        # Comando
        cmd_text = 'libreoffice --headless --convert-to pdf --outdir docs "docs/Git - Comandos e Merge com conflito.odp"'
        cmd_style = ParagraphStyle(
            'CodeStyle',
            parent=styles['Normal'],
            fontName='Courier',
            fontSize=9,
            textColor=colors.HexColor('#333333'),
            backColor=colors.HexColor('#f0f0f0'),
            leftIndent=20,
        )
        story.append(Paragraph(cmd_text, cmd_style))
        
        story.append(Spacer(1, 20))
        
        # Nota
        note_style = ParagraphStyle(
            'NoteStyle',
            parent=styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#cc0000'),
        )
        story.append(Paragraph(
            "⚠️ <b>Nota</b>: Este PDF é um documento informativo. Para visualizar o conteúdo original da apresentação, abra o arquivo ODP no LibreOffice ou converta usando um dos métodos acima.",
            note_style
        ))
        
        # Construir PDF
        doc.build(story)
        print(f"✅ PDF criado com sucesso: {output_file}")
        return True
        
    except ImportError:
        print("❌ ReportLab não disponível")
        return False
    except Exception as e:
        print(f"❌ Erro ao criar PDF: {e}")
        return False

def main():
    # Definir caminhos
    current_dir = Path(__file__).parent
    input_file = current_dir / "docs" / "Git - Comandos e Merge com conflito.odp"
    output_dir = current_dir / "docs"
    
    # Verificar se arquivo existe
    if not input_file.exists():
        print(f"❌ Arquivo não encontrado: {input_file}")
        return False
    
    print(f"📄 Arquivo de entrada: {input_file.name}")
    print(f"📁 Diretório de saída: {output_dir}")
    print()
    
    # Tentar conversão com LibreOffice
    if convert_with_libreoffice_cli(str(input_file), str(output_dir)):
        return True
    
    print("\n⚠️  LibreOffice não encontrado ou falhou na conversão.")
    print("   Criando PDF informativo alternativo...\n")
    
    # Criar PDF informativo
    if create_pdf_with_reportlab(str(input_file), str(output_dir)):
        print("\n💡 Dica: Para converter o ODP original, instale LibreOffice em:")
        print("   https://www.libreoffice.org/")
        return True
    
    return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
