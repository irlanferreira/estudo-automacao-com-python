import docx

# Criando objeto document
documento = docx.Document('demo.docx')
# Variável com objeto paragraph
paragrafo2 = documento.paragraphs[1]
# Conteúdo do paragrafo
paragrafo2.text
# Pegando runs
paragrafo2.runs
paragrafo2.runs[2].text
