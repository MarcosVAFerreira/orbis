# src/api/app.py
from flask import Flask, jsonify, request
from src.usuarios import UsuarioRepo
from src.contas import ContaRepo
from src.transacoes import TransacaoService

app = Flask(__name__)

# Repositórios em memória (para protótipo)
usuario_repo = UsuarioRepo()
conta_repo = ContaRepo()
transacao_service = TransacaoService(conta_repo)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/users", methods=["POST"])
def create_user():
    data = request.json or {}
    username = data.get("username")
    full_name = data.get("full_name")
    if not username:
        return jsonify({"error": "username required"}), 400

    # evita duplicados por username neste repositório simples
    existing = usuario_repo.find_by_username(username)
    if existing:
        return jsonify({"error": "username exists", "user_id": existing.id}), 409

    u = usuario_repo.create(username, full_name=full_name)
    c = conta_repo.create(u.id, "BRL")  # conta BRL padrão
    return jsonify({"user_id": u.id, "account_id": c.id}), 200


@app.route("/accounts/<account_id>", methods=["GET"])
def get_account(account_id):
    try:
        c = conta_repo.get(account_id)
        return jsonify(c.dict()), 200
    except Exception:
        return jsonify({"error": "account not found"}), 404


@app.route("/accounts/<account_id>/deposit", methods=["POST"])
def deposit(account_id):
    data = request.json or {}
    amount = data.get("amount")
    try:
        amount = float(amount)
    except Exception:
        return jsonify({"error": "invalid amount"}), 400

    if amount <= 0:
        return jsonify({"error": "amount must be > 0"}), 400

    try:
        t = transacao_service.deposit(account_id, amount, "BRL")
        return jsonify(t.dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/accounts/<account_id>/withdraw", methods=["POST"])
def withdraw(account_id):
    data = request.json or {}
    amount = data.get("amount")
    try:
        amount = float(amount)
    except Exception:
        return jsonify({"error": "invalid amount"}), 400

    if amount <= 0:
        return jsonify({"error": "amount must be > 0"}), 400

    try:
        t = transacao_service.withdraw(account_id, amount, "BRL")
        return jsonify(t.dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    # porta 5000 por padrão; em produção use gunicorn/uvicorn
    app.run(host="0.0.0.0", port=5000, debug=True)
