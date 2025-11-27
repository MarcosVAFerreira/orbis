from typing import Dict, List
from pydantic import BaseModel
import uuid


class Conta(BaseModel):
id: str
user_id: str
currency: str
balance: float = 0.0
label: str = ''




class ContaRepo:
def __init__(self):
self._contas: Dict[str, Conta] = {}


def create(self, user_id: str, currency: str, label: str = '') -> Conta:
c = Conta(id=str(uuid.uuid4()), user_id=user_id, currency=currency.upper(), balance=0.0, label=label)
self._contas[c.id] = c
return c


def get_for_user(self, user_id: str) -> List[Conta]:
return [c for c in self._contas.values() if c.user_id == user_id]


def get(self, conta_id: str) -> Conta:
return self._contas[conta_id]


def update_balance(self, conta_id: str, new_balance: float):
c = self._contas[conta_id]
c.balance = new_balance
self._contas[conta_id] = c
return c