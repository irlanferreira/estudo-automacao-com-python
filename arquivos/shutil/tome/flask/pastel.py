import json, requests
livros = requests.get("http://localhost:5000/livros").content
livros = json.loads(livros)
for l in livros:
    print(f"Id: {l['id']}\nNome: {l['titulo']}\nAutor: {l['autor']}\n")