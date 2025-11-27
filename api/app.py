from flask import Flask, request, jsonify
from src.usuarios import UsuarioRepo

app = Flask(__name__)
repo = UsuarioRepo()

@app.get("/usuarios")
def listar():
    return jsonify([u.__dict__ for u in repo.listar()])

@app.post("/usuarios")
def criar():
    dados = request.json
    usuario = repo.criar(dados["nome"], dados["email"])
    return jsonify(usuario.__dict__), 201

@app.get("/usuarios/<id>")
def obter(id):
    usuario = repo.obter(id)
    if usuario:
        return jsonify(usuario.__dict__)
    return {"erro": "Usuário não encontrado"}, 404

@app.delete("/usuarios/<id>")
def deletar(id):
    if repo.remover(id):
        return "", 204
    return {"erro": "Usuário não encontrado"}, 404

if __name__ == "__main__":
    app.run(debug=True)
