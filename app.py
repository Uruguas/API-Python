from flask import Flask, jsonify, request


app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O senhor dos Aneis',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'O poder do Habito',
        'autor': 'Charles Duhigg'
    },
    {
        'id': 3,
        'titulo': 'A arte da guerra',
        'autor': 'Sun Tzu'
    },
]


# Consultar(Todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
# Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
# Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def ecluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5000,host='localhost', debug=True)
