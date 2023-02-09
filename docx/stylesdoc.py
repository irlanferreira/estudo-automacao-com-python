import docx

document = docx.Document('demo.docx')

document.paragraphs[1].runs[0].style = "Quote Char"
document.paragraphs[1].runs[4].underline = True
document.save('editado.docx')
