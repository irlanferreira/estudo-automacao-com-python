import os
caminho = os.path.abspath("..\\SQLite")
arq = open(caminho + "\\teste.txt", "r")
conteudo = arq.read()
conteudoLista = arq.readlines()
print(conteudo)
print(conteudoLista)