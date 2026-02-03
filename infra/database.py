"""
Modelos de persistência - SQLAlchemy
"""
from datetime import datetime
from sqlalchemy import (
    Column, String, DateTime, Boolean, 
    Numeric, Enum, ForeignKey, Text
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum

Base = declarative_base()


class CurrencyEnum(str, enum.Enum):
    BRL = "BRL"
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"


class TransactionTypeEnum(str, enum.Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    TRANSFER = "TRANSFER"
    CONVERSION = "CONVERSION"


class AccountStatusEnum(str, enum.Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    CLOSED = "CLOSED"


class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True)
    email = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    
    accounts = relationship("AccountModel", back_populates="user")


class AccountModel(Base):
    __tablename__ = "accounts"
    
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    currency = Column(Enum(CurrencyEnum), nullable=False)
    label = Column(String, nullable=False)
    status = Column(Enum(AccountStatusEnum), default=AccountStatusEnum.ACTIVE)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("UserModel", back_populates="accounts")
    transactions = relationship("TransactionModel", back_populates="account")


class TransactionModel(Base):
    __tablename__ = "transactions"
    
    id = Column(String, primary_key=True)
    account_id = Column(String, ForeignKey("accounts.id"), nullable=False)
    type = Column(Enum(TransactionTypeEnum), nullable=False)
    amount = Column(Numeric(precision=18, scale=2), nullable=False)
    currency = Column(Enum(CurrencyEnum), nullable=False)
    balance_after = Column(Numeric(precision=18, scale=2), nullable=False)
    description = Column(String)
    metadata = Column(Text)  # JSON
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    
    account = relationship("AccountModel", back_populates="transactions")
