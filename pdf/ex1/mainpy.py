import os, PyPDF2

arquivoslista = os.listdir('.//pdfs')
arquivoslista.sort()

novopdf = PyPDF2.PdfWriter()

for arq in arquivoslista:
    if arq.endswith('.pdf'):
        pdfler = PyPDF2.PdfReader(open(f'.//pdfs//{arq}', 'rb'))
        for pagnum in range(1, len(pdfler.pages)):
            print(f"Adicionando página {pagnum} do documento {arq}...")
            novopdf.add_page(pdfler.pages[pagnum])

output = open('resultado.pdf', 'wb')
novopdf.write(output)
