import os, shutil, csv

arqs = os.listdir('.//arquivos')
for arq in arqs:
    if arq.endswith('.csv') and not '_MODIFICADO.csv' in arq:
        nomearq = os.path.splitext(arq)[0]
        objreader = csv.reader(open(f'.//arquivos//{arq}'))
        content = list(objreader)

        objwriter = csv.writer(open(f'.//arquivos//{nomearq}_MODIFICADO.csv', 'w', newline=''))
        for l in range(0, len(content)):
            if l == 0:
                pass
            else:
                objwriter.writerow(content[l])
