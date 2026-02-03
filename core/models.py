"""
Modelos de domínio do Orbis
Sem dependências de framework - apenas Python puro
"""
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from uuid import uuid4


class Currency(str, Enum):
    BRL = "BRL"
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"


class TransactionType(str, Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    TRANSFER = "TRANSFER"
    CONVERSION = "CONVERSION"


class AccountStatus(str, Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    CLOSED = "CLOSED"


@dataclass
class User:
    """Entidade de usuário"""
    id: str = field(default_factory=lambda: str(uuid4()))
    email: str = ""
    name: str = ""
    password_hash: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    is_active: bool = True


@dataclass
class Account:
    """Conta bancária multi-moeda"""
    id: str = field(default_factory=lambda: str(uuid4()))
    user_id: str = ""
    currency: Currency = Currency.BRL
    label: str = ""
    status: AccountStatus = AccountStatus.ACTIVE
    created_at: datetime = field(default_factory=datetime.utcnow)
    
    def __post_init__(self):
        if not self.label:
            self.label = f"Conta {self.currency.value}"


@dataclass
class Transaction:
    """Transação imutável - base do ledger"""
    id: str = field(default_factory=lambda: str(uuid4()))
    account_id: str = ""
    type: TransactionType = TransactionType.DEPOSIT
    amount: Decimal = Decimal("0")
    currency: Currency = Currency.BRL
    balance_after: Decimal = Decimal("0")
    description: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    metadata: dict = field(default_factory=dict)
    
    def __post_init__(self):
        # Garante que amount seja Decimal
        if not isinstance(self.amount, Decimal):
            self.amount = Decimal(str(self.amount))
        if not isinstance(self.balance_after, Decimal):
            self.balance_after = Decimal(str(self.balance_after))


@dataclass
class ConsolidatedBalance:
    """Saldo consolidado em BRL"""
    total_brl: Decimal = Decimal("0")
    accounts: List[dict] = field(default_factory=list)
    updated_at: datetime = field(default_factory=datetime.utcnow)
