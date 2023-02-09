import requests, bs4, time, os, threading

linkorig = 'https://xkcd.com'
dpsbarra = ''

def salvar(ditocujo, nome):
    if os.path.exists('.//tirinhas'):
        pass
    else:
        os.makedirs('.//tirinhas')
    for chunk in ditocujo.iter_content(500000):
        print(f"Salvando {nome} no disco...")
        with open(f'.//tirinhas//{nome}', 'wb') as arq:
            arq.write(chunk)
    print(f"{nome} salvo com sucesso!")


while True:
    link = f"{linkorig}{dpsbarra}"
    html = requests.get(link)
    sopinha = bs4.BeautifulSoup(html.text, features='html.parser')
    img = sopinha.select('div#comic img')[0]
    imglink = 'https:'+img.get('src')
    imgreq = requests.get(imglink)
    imgnome = os.path.split(imglink)[1]
    print(f'Baixando {imgnome}...')
    dpsbarra = sopinha.select('ul.comicNav li a')[1].get('href')
    salvarthread = threading.Thread(target=salvar, args=[imgreq, imgnome])
    salvarthread.start()