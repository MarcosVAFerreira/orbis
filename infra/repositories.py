"""
Repositórios - Camada de acesso a dados
"""
import json
from decimal import Decimal
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import desc

from .database import UserModel, AccountModel, TransactionModel
from core.models import User, Account, Transaction, Currency


class UserRepository:
    """Repositório de usuários"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, user: User) -> User:
        """Cria um usuário"""
        db_user = UserModel(
            id=user.id,
            email=user.email,
            name=user.name,
            password_hash=user.password_hash,
            created_at=user.created_at,
            is_active=user.is_active
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return self._to_domain(db_user)
    
    def get_by_email(self, email: str) -> Optional[User]:
        """Busca usuário por email"""
        db_user = self.db.query(UserModel).filter(UserModel.email == email).first()
        return self._to_domain(db_user) if db_user else None
    
    def get_by_id(self, user_id: str) -> Optional[User]:
        """Busca usuário por ID"""
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        return self._to_domain(db_user) if db_user else None
    
    @staticmethod
    def _to_domain(db_user: UserModel) -> User:
        """Converte modelo de BD para domínio"""
        return User(
            id=db_user.id,
            email=db_user.email,
            name=db_user.name,
            password_hash=db_user.password_hash,
            created_at=db_user.created_at,
            is_active=db_user.is_active
        )


class AccountRepository:
    """Repositório de contas"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, account: Account) -> Account:
        """Cria uma conta"""
        db_account = AccountModel(
            id=account.id,
            user_id=account.user_id,
            currency=account.currency,
            label=account.label,
            status=account.status,
            created_at=account.created_at
        )
        self.db.add(db_account)
        self.db.commit()
        self.db.refresh(db_account)
        return self._to_domain(db_account)
    
    def get_by_user(self, user_id: str) -> List[Account]:
        """Busca todas as contas de um usuário"""
        db_accounts = self.db.query(AccountModel).filter(
            AccountModel.user_id == user_id
        ).all()
        return [self._to_domain(acc) for acc in db_accounts]
    
    def get_by_id(self, account_id: str) -> Optional[Account]:
        """Busca conta por ID"""
        db_account = self.db.query(AccountModel).filter(
            AccountModel.id == account_id
        ).first()
        return self._to_domain(db_account) if db_account else None
    
    @staticmethod
    def _to_domain(db_account: AccountModel) -> Account:
        """Converte modelo de BD para domínio"""
        return Account(
            id=db_account.id,
            user_id=db_account.user_id,
            currency=Currency(db_account.currency.value),
            label=db_account.label,
            status=db_account.status,
            created_at=db_account.created_at
        )


class TransactionRepository:
    """Repositório de transações"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, transaction: Transaction) -> Transaction:
        """Cria uma transação"""
        db_transaction = TransactionModel(
            id=transaction.id,
            account_id=transaction.account_id,
            type=transaction.type,
            amount=transaction.amount,
            currency=transaction.currency,
            balance_after=transaction.balance_after,
            description=transaction.description,
            metadata=json.dumps(transaction.metadata),
            created_at=transaction.created_at
        )
        self.db.add(db_transaction)
        self.db.commit()
        self.db.refresh(db_transaction)
        return self._to_domain(db_transaction)
    
    def get_by_account(self, account_id: str, limit: int = 100) -> List[Transaction]:
        """Busca transações de uma conta"""
        db_transactions = self.db.query(TransactionModel).filter(
            TransactionModel.account_id == account_id
        ).order_by(desc(TransactionModel.created_at)).limit(limit).all()
        return [self._to_domain(tx) for tx in db_transactions]
    
    @staticmethod
    def _to_domain(db_transaction: TransactionModel) -> Transaction:
        """Converte modelo de BD para domínio"""
        return Transaction(
            id=db_transaction.id,
            account_id=db_transaction.account_id,
            type=db_transaction.type,
            amount=Decimal(str(db_transaction.amount)),
            currency=Currency(db_transaction.currency.value),
            balance_after=Decimal(str(db_transaction.balance_after)),
            description=db_transaction.description,
            metadata=json.loads(db_transaction.metadata) if db_transaction.metadata else {},
            created_at=db_transaction.created_at
        )
