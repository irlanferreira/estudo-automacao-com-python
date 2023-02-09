import docx
from docx.shared import Pt

with open('convidados.txt', 'r') as file:
    convidados = file.read().split('\n')

documento = docx.Document('modelo.docx')
for convidado in convidados:
    parag = documento.add_paragraph(f'Eu quero a presença de')
    parag.style = 'convite'
    parag = documento.add_paragraph(convidado)
    parag.style = 'convite'
    parag = documento.add_paragraph('No meu chá de fraldas')
    parag.style = 'convite'
    parag.runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)
documento.save('convites.docx')
