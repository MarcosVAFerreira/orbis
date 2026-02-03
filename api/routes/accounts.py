"""
Rotas de contas bancárias
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import AccountCreate, AccountResponse
from ..auth import get_current_user
from core.models import User
from core.services import AccountService, TransactionService
from infra.repositories import AccountRepository, TransactionRepository

router = APIRouter()


@router.post("/", response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
def create_account(
    account_data: AccountCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Cria uma nova conta"""
    account_repo = AccountRepository(db)
    
    # Cria conta via serviço de domínio
    account = AccountService.create_account(
        user_id=current_user.id,
        currency=account_data.currency,
        label=account_data.label
    )
    
    created_account = account_repo.create(account)
    
    return AccountResponse(
        id=created_account.id,
        user_id=created_account.user_id,
        currency=created_account.currency,
        label=created_account.label,
        status=created_account.status,
        balance=0,
        created_at=created_account.created_at
    )


@router.get("/", response_model=List[AccountResponse])
def list_accounts(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Lista todas as contas do usuário"""
    account_repo = AccountRepository(db)
    transaction_repo = TransactionRepository(db)
    
    accounts = account_repo.get_by_user(current_user.id)
    
    response = []
    for account in accounts:
        # Calcula saldo a partir do ledger
        transactions = transaction_repo.get_by_account(account.id)
        balance = TransactionService.calculate_balance(transactions)
        
        response.append(AccountResponse(
            id=account.id,
            user_id=account.user_id,
            currency=account.currency,
            label=account.label,
            status=account.status,
            balance=balance,
            created_at=account.created_at
        ))
    
    return response


@router.get("/{account_id}", response_model=AccountResponse)
def get_account(
    account_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Busca uma conta específica"""
    account_repo = AccountRepository(db)
    transaction_repo = TransactionRepository(db)
    
    account = account_repo.get_by_id(account_id)
    
    if not account or account.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    
    transactions = transaction_repo.get_by_account(account.id)
    balance = TransactionService.calculate_balance(transactions)
    
    return AccountResponse(
        id=account.id,
        user_id=account.user_id,
        currency=account.currency,
        label=account.label,
        status=account.status,
        balance=balance,
        created_at=account.created_at
    )
