import PyPDF2

pdfminutes = PyPDF2.PdfReader(open('meetingminutes.pdf', 'rb'))
pdfmarca = PyPDF2.PdfReader(open('watermark.pdf', 'rb'))

novopdf = PyPDF2.PdfWriter()

minutespag1 = pdfminutes.pages[0]
pagmarca = pdfmarca.pages[0]
minutespag1.merge_page(pagmarca)

novopdf.add_page(minutespag1)

for numpage in range(1, len(pdfminutes.pages)):
    novopdf.add_page(pdfminutes.pages[numpage])

output = open('commarca.pdf', 'wb')
novopdf.write(output)