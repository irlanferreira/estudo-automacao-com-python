import os, shutil, send2trash

for pasta, subpasta, arquivo in os.walk('pastadoxd'):
    for arq in arquivo:
        path = f"{pasta}\\{arq}"
        tamanho = os.path.getsize(path) / 1000000
        if tamanho > 100 :
            send2trash.send2trash(path)
            print(f"Deletando {arq}...")
