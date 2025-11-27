from data.memory_db import DB
import uuid

class UsuarioRepo:

    def listar(self):
        return DB["usuarios"]

    def criar(self, nome, email):
        novo = {
            "id": str(uuid.uuid4()),
            "nome": nome,
            "email": email
        }
        DB["usuarios"].append(novo)
        return novo

    def deletar(self, id):
        DB["usuarios"] = [u for u in DB["usuarios"] if u["id"] != id]
        return True
