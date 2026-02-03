"""
Schemas Pydantic - Contratos da API
"""
from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field

from core.models import Currency, TransactionType, AccountStatus


# ============ Auth ============
class UserRegister(BaseModel):
    email: EmailStr
    name: str
    password: str = Field(..., min_length=6)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: str
    email: str
    name: str
    created_at: datetime
    is_active: bool


# ============ Accounts ============
class AccountCreate(BaseModel):
    currency: Currency
    label: Optional[str] = None


class AccountResponse(BaseModel):
    id: str
    user_id: str
    currency: Currency
    label: str
    status: AccountStatus
    balance: Decimal
    created_at: datetime


# ============ Transactions ============
class TransactionCreate(BaseModel):
    account_id: str
    type: TransactionType
    amount: Decimal = Field(..., gt=0)
    description: Optional[str] = None


class TransactionResponse(BaseModel):
    id: str
    account_id: str
    type: TransactionType
    amount: Decimal
    currency: Currency
    balance_after: Decimal
    description: str
    created_at: datetime


# ============ Dashboard ============
class ConsolidatedBalanceResponse(BaseModel):
    total_brl: Decimal
    accounts: List[dict]
    updated_at: datetime


class DashboardResponse(BaseModel):
    user: UserResponse
    consolidated_balance: ConsolidatedBalanceResponse
    recent_transactions: List[TransactionResponse]
