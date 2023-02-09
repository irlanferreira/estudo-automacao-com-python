import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
for chunk in res.iter_content(100000):
    with open('gnomeu.txt', 'wb')as arq:
        arq.write(chunk)