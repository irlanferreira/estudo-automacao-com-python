import bs4, requests

res = open('example.html')
sopa = bs4.BeautifulSoup(res.read())
elementos = sopa.select('p')
print(elementos[0].get_text())