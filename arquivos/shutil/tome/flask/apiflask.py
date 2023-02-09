from flask import Flask, request
import json

aplicativo = Flask(__name__)
livros = [
    {
        'id': 1,
        'titulo': 'Essencialismo',
        'autor': 'Greg McKeown'
    },
    {
        'id': 2,
        'titulo': '12 Regras para a vida',
        'autor': 'Jordan Peterson'
    },
    {
        'id': 3,
        'titulo': 'Pai Rico Pai Pobre',
        'autor': 'Robert T.'
    }
]
#Consultar Todos
@aplicativo.route('/livros',methods=['GET'])
def obterLivros():
    return (json.dumps(livros))

@aplicativo.route('/livros/<int:id>', methods=['GET'])
def obterLivroId(id):
    for l in livros:
        if l.get('id') == id:
            return json.dumps(l)

@aplicativo.route("/livros/<int:id>", methods=['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    for i, l in enumerate(livros):
        if l.get('id') == id:
            livros[i].update(livro_alterado)
            return json.dumps(livros[i])

@aplicativo.route("/livros", methods=['POST'])
def adicionarLivro():
    livro = request.get_json()
    livros.append(livro)
    return livros

@aplicativo.route("/livros/<int:id>", methods=['DELETE'])
def deletarLivro(id):
    for i, l in enumerate(livros):
        if id == l.get('id'):
            del livros[i]
            return livros

aplicativo.run(port=5000,host='localhost',debug=True)