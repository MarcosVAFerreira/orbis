from typing import List
from pydantic import BaseModel
from datetime import datetime


class Transacao(BaseModel):
id: str
conta_id: str
amount: float
currency: str
type: str # deposit, withdraw
created_at: str




class TransacaoService:
def __init__(self, conta_repo):
self._log: List[Transacao] = []
self.conta_repo = conta_repo


def deposit(self, conta_id: str, amount: float, currency: str) -> Transacao:
conta = self.conta_repo.get(conta_id)
if amount <= 0:
raise ValueError("Amount must be positive")
conta.balance += amount
self.conta_repo.update_balance(conta_id, conta.balance)
t = Transacao(id=str(len(self._log) + 1), conta_id=conta_id, amount=amount, currency=currency, type='deposit', created_at=datetime.utcnow().isoformat()+'Z')
self._log.append(t)
return t


def withdraw(self, conta_id: str, amount: float, currency: str) -> Transacao:
conta = self.conta_repo.get(conta_id)
if amount <= 0:
raise ValueError("Amount must be positive")
if conta.balance < amount:
raise ValueError("Insufficient funds")
conta.balance -= amount
self.conta_repo.update_balance(conta_id, conta.balance)
t = Transacao(id=str(len(self._log) + 1), conta_id=conta_id, amount=amount, currency=currency, type='withdraw', created_at=datetime.utcnow().isoformat()+'Z')
self._log.append(t)
return t


def extrato(self, conta_id: str):
return [t for t in self._log if t.conta_id == conta_id]