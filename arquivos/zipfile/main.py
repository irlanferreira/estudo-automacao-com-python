import os, zipfile

with zipfile.ZipFile('kipi.zip', 'w') as arq:
    arq.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
    arq.write('main.py', compress_type=zipfile.ZIP_DEFLATED)
zipado = zipfile.ZipFile('.\\kipi.zip')
print(zipado.namelist())