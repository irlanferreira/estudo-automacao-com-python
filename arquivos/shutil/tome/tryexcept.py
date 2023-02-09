x = 50
try:
    print(x)
except NameError:
    print("X Não definido")
except:
    print("Erro desconhecido")
else:
    print("Tudo certo")