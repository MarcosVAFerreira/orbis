from typing import Dict, Optional
from pydantic import BaseModel
import uuid


class Usuario(BaseModel):
id: str
username: str
full_name: Optional[str]




class UsuarioRepo:
def __init__(self):
self._users: Dict[str, Usuario] = {}


def create(self, username: str, full_name: Optional[str] = None) -> Usuario:
user = Usuario(id=str(uuid.uuid4()), username=username, full_name=full_name)
self._users[user.id] = user
return user


def get(self, user_id: str) -> Optional[Usuario]:
return self._users.get(user_id)


def find_by_username(self, username: str) -> Optional[Usuario]:
for u in self._users.values():
if u.username == username:
return u
return None