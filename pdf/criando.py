import PyPDF2

# Abrindo file dos pdfs originais
pdffile1 = open('meetingminutes.pdf', 'rb')
pdffile2 = open('meetingminutes2.pdf', 'rb')

# Criando o obj pdfreader dos documentos originais
pdf1reader = PyPDF2.PdfReader(pdffile1)
pdf2reader = PyPDF2.PdfReader(pdffile2)

# Criando o objeto do novo pdf
pdfWriter = PyPDF2.PdfWriter()

# Copiando as páginas dos documentos originais para o novo documento
for pageNum in range(len(pdf1reader.pages)):
    page = pdf1reader.pages[pageNum]
    # Rotacionar página
    # page.rotate(90)

    # Adicionado página
    pdfWriter.add_page(page)
for pageNum in range(len(pdf2reader.pages)):
    page = pdf2reader.pages[pageNum]
    # Adicionado página
    pdfWriter.add_page(page)
# Abrindo file do novo pdf
output = open('pdf.pdf', 'wb')
# Escrevendo no novo pdf
pdfWriter.write(output)
