import bs4, os, shutil, requests

dpsbarra = ''
cont = 0
link = 'https://xkcd.com'

while True:
    pagina = requests.get(f'{link}{dpsbarra}')
    pagina.raise_for_status()

    sopa = bs4.BeautifulSoup(pagina.text, features="html.parser")
    prevelem = sopa.select('ul.comicNav a[rel="prev"]')
    if prevelem == '#':
        break
    else:
        imglink = 'https:' + sopa.select('div#comic img')[0].get('src')
        img = requests.get(imglink)
        for chunk in img.iter_content(1000000):
            imagemnome = os.path.split(imglink)[1]
            os.makedirs('.\\tirinhas') if not os.path.exists('.\\tirinhas') else img
            with open(f'.\\tirinhas\\{imagemnome}', 'wb') as arq:
                arq.write(chunk)
            print(f'Imagem {imagemnome} salva com sucesso.')
        dpsbarra = prevelem[0].get('href')
