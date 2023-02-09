import PyPDF2

# Abrindo o arquivo em modo binário de leitura
arq = open('meetingminutes.pdf', 'rb')
# Criando um objeto objpdf
objpdf = PyPDF2.PdfReader(arq)
# Verificando se o pdf é criptografado
objpdf.is_encrypted
# Obtendo o numero de paginas do documento
paginasqtd = len(objpdf.pages)
# Obtendo objeto de uma página
pag = objpdf.pages[1]
# Extraindo texto
text = pag.extract_text()
print(text)

# Pdf criptografado
crippdf = PyPDF2.PdfReader(open('encrypted.pdf', 'rb'))
# Descriptografando
crippdf.decrypt('rosebud')
# Lendo
page = crippdf.pages[1]
print(page.extract_text())
