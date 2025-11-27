from dataclasses import dataclass
from typing import Dict, Optional
import uuid

@dataclass
class Usuario:
    id: str
    nome: str
    email: str

class UsuarioRepo:
    def __init__(self):
        # Banco de dados em memória
        self._usuarios: Dict[str, Usuario] = {}

    def criar(self, nome: str, email: str) -> Usuario:
        novo_id = str(uuid.uuid4())
        usuario = Usuario(id=novo_id, nome=nome, email=email)
        self._usuarios[novo_id] = usuario
        return usuario

    def listar(self):
        return list(self._usuarios.values())

    def obter(self, usuario_id: str) -> Optional[Usuario]:
        return self._usuarios.get(usuario_id)

    def remover(self, usuario_id: str) -> bool:
        if usuario_id in self._usuarios:
            del self._usuarios[usuario_id]
            return True
        return False
