from flask import Flask
from api.controllers.usuarios import usuarios_bp
from api.controllers.contas import contas_bp
from api.controllers.transacoes import transacoes_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(usuarios_bp, url_prefix="/usuarios")
    app.register_blueprint(contas_bp, url_prefix="/contas")
    app.register_blueprint(transacoes_bp, url_prefix="/transacoes")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
