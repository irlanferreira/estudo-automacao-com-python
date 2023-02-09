import webbrowser, bs4, requests
pesquisa = input('Qual anime deseja procurar?: ')
link = f'https://betteranime.net/pesquisa?titulo={pesquisa}&searchTerm={pesquisa}'
pag = requests.get(link)
pag.raise_for_status()
sopabonita = bs4.BeautifulSoup(pag.text, features="html.parser")
elms = sopabonita.select('div.card-vertical h3')
for el in elms:
    print(el.get_text())