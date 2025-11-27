from flask import Blueprint, request, jsonify
from core.usuarios import UsuarioRepo

usuarios_bp = Blueprint("usuarios", __name__)
repo = UsuarioRepo()

@usuarios_bp.get("/")
def listar():
    return jsonify(repo.listar())

@usuarios_bp.post("/")
def criar():
    data = request.json
    resp = repo.criar(data["nome"], data["email"])
    return jsonify(resp)

@usuarios_bp.delete("/<id>")
def deletar(id):
    repo.deletar(id)
    return {"status": "ok"}
