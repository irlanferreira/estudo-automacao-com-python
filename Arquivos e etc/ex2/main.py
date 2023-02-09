import os, shutil, random, re

#for i in range(0, 42):
#    mes = random.randint(1, 12)
#     dia = random.randint(1,30)
#    with open(f".\\arquivos\\folhas de ponto-{'0' if mes < 10 else ''}{mes}-{'0' if dia < 10 else ''}{dia}-{random.randint(1958, 2022)}.txt", 'a') as arq:
#        pass

datareg = re.compile(r"""^
(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*?)
$""", re.VERBOSE)
arqs = os.listdir(".\\arquivos")
for arq in arqs:
    textoin = datareg.search(arq).group(1)
    mes = datareg.search(arq).group(2)
    dia = datareg.search(arq).group(4)
    ano = datareg.search(arq).group(6)
    textofim = datareg.search(arq).group(8)
    novoNome = textoin+dia+'-'+mes+'-'+ano+textofim
    shutil.move(f".\\arquivos\\{arq}", f".\\arquivos\\{novoNome}")