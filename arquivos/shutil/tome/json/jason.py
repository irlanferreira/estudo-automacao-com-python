import requests
import json

arq = open("pessoa.json", "r")
pessoa_json = arq.read()
pessoa_dict = json.loads(pessoa_json)
print(pessoa_dict['Dispositivos'][1])
dados = requests.get("https://random-data-api.com/api/v2/users").content
dados_dict = json.loads(dados)
print(f"Nome: {dados_dict['first_name']}\nSobrenome: {dados_dict['last_name']}\nE-mail: {dados_dict['email']}")