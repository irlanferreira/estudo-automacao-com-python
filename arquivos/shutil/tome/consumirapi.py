import json, requests
dados = requests.get("https://randomuser.me/api/").content
dict = json.loads(dados)
print(dict['results'][0]['name'])