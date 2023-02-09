import docx

document = docx.Document('demo.docx')
# Inserindo paragrafo antes de outro paragrafo
document.paragraphs[2].insert_paragraph_before('Esse paragrafo vai antes')
# Adicionando títulos
titlehello = document.add_paragraph('Hello world!', 'Title')
headinghello = document.add_heading('Olá mundo!', 0)
# Adicionando paragrafo no fim do documento
para = document.add_paragraph('Joji')
para.add_run(' É o melhor cantor.')
# Quebrando página
para.runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)
document.add_paragraph('eeee naaaaadaaaaa')
# Adicionando imagens
document.add_picture('cachorroacademi.jpeg', width=docx.shared.Cm(2), height=docx.shared.Cm(2))

document.save('escrito.docx')

