import shutil, os, send2trash

for arq in os.listdir(".\\POO"):
    print(arq)
    if arq.endswith(".py"):
        send2trash.send2trash(f".\\POO\\{arq}")