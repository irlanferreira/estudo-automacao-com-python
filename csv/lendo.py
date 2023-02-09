import csv

arq = csv.reader(open('example.csv'))
for l in arq:
    print(f"Linha {arq.line_num}: {l}")
