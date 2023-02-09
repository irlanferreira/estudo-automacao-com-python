import os, shutil, zipfile, re

projetoNome = "projetomaneiro"
regzipnome = re.compile(r"(projetomaneiro)(\d{1,3})(.zip)")
arqs = os.listdir('.\\')
for arq in arqs:
    if regzipnome.search(arq):
        numatual = regzipnome.search(arq).group(2)
    else:
        numatual = 0
ziparq = zipfile.ZipFile(f".\\projetomaneiro{'1'if numatual==0 else int(numatual)+1}.zip", 'w')
for i in os.listdir('projetomaneiro'):
    ziparq.write(f".\\projetomaneiro\\{i}", compress_type=zipfile.ZIP_DEFLATED)