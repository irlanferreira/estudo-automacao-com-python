import os, PyPDF2

for root, pastas, arquivos in os.walk('.//pdfs'):
    for arq in arquivos:
        patharq = f"{root}\{arq}"
        nomearq = os.path.splitext(arq)[0]
        if arq.endswith('.pdf'):
            with open(patharq, 'rb') as file:
                if PyPDF2.PdfReader(file).is_encrypted:
                    crypted = True
                else:
                    crypted = False
            if not crypted:
                with open(patharq, 'wb') as file:
                    document = PyPDF2.PdfWriter(file)
                    document.encrypt(input(f'Qual senha deseja inserir no arquivo {arq}?: '))
                    with open(f"{root}\{nomearq}_CRIPTOGRAFADO.pdf", 'wb') as output:
                        document.write(output)
print('\nTodos os arquivos foram criptografados corretamente! Inicianto modo de teste...')
for root, pastas, arquivos in os.walk('.//pdfs'):
    for arq in arquivos:
        if '_CRIPTOGRAFADO.pdf' in arq:
            pdf = PyPDF2.PdfReader
            if pdf.is_encrypted:
                print(f"\nO arquivo {arq} está criptografado com segurança.")