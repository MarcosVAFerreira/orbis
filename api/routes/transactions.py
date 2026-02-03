"""
Rotas de transações
"""
from typing import List
from decimal import Decimal
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import (
    TransactionCreate, TransactionResponse,
    DashboardResponse, ConsolidatedBalanceResponse, UserResponse
)
from ..auth import get_current_user
from core.models import User, TransactionType
from core.services import TransactionService, ConsolidationService
from infra.repositories import AccountRepository, TransactionRepository

router = APIRouter()


@router.post("/", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
def create_transaction(
    transaction_data: TransactionCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Cria uma nova transação"""
    account_repo = AccountRepository(db)
    transaction_repo = TransactionRepository(db)
    
    # Valida conta
    account = account_repo.get_by_id(transaction_data.account_id)
    if not account or account.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    
    # Calcula saldo atual
    transactions = transaction_repo.get_by_account(account.id)
    current_balance = TransactionService.calculate_balance(transactions)
    
    # Cria transação via serviço de domínio
    try:
        if transaction_data.type == TransactionType.DEPOSIT:
            transaction = TransactionService.create_deposit(
                account_id=account.id,
                amount=transaction_data.amount,
                currency=account.currency,
                description=transaction_data.description
            )
        elif transaction_data.type == TransactionType.WITHDRAWAL:
            transaction = TransactionService.create_withdrawal(
                account_id=account.id,
                amount=transaction_data.amount,
                currency=account.currency,
                current_balance=current_balance,
                description=transaction_data.description
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Transaction type not supported"
            )
        
        # Atualiza balance_after
        if transaction.type == TransactionType.DEPOSIT:
            transaction.balance_after = current_balance + transaction.amount
        else:
            transaction.balance_after = current_balance - transaction.amount
        
        created_transaction = transaction_repo.create(transaction)
        
        return TransactionResponse(
            id=created_transaction.id,
            account_id=created_transaction.account_id,
            type=created_transaction.type,
            amount=created_transaction.amount,
            currency=created_transaction.currency,
            balance_after=created_transaction.balance_after,
            description=created_transaction.description,
            created_at=created_transaction.created_at
        )
    
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/account/{account_id}", response_model=List[TransactionResponse])
def list_transactions(
    account_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Lista transações de uma conta"""
    account_repo = AccountRepository(db)
    transaction_repo = TransactionRepository(db)
    
    # Valida conta
    account = account_repo.get_by_id(account_id)
    if not account or account.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    
    transactions = transaction_repo.get_by_account(account_id)
    
    return [
        TransactionResponse(
            id=tx.id,
            account_id=tx.account_id,
            type=tx.type,
            amount=tx.amount,
            currency=tx.currency,
            balance_after=tx.balance_after,
            description=tx.description,
            created_at=tx.created_at
        )
        for tx in transactions
    ]


@router.get("/dashboard", response_model=DashboardResponse)
def get_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Retorna dados do dashboard"""
    account_repo = AccountRepository(db)
    transaction_repo = TransactionRepository(db)
    
    # Busca contas
    accounts = account_repo.get_by_user(current_user.id)
    
    # Prepara dados para consolidação
    accounts_data = []
    all_transactions = []
    
    for account in accounts:
        transactions = transaction_repo.get_by_account(account.id)
        balance = TransactionService.calculate_balance(transactions)
        
        accounts_data.append({
            "currency": account.currency,
            "balance": balance
        })
        
        all_transactions.extend(transactions)
    
    # Consolida saldos
    consolidated = ConsolidationService.consolidate_balance(accounts_data)
    
    # Ordena transações recentes
    all_transactions.sort(key=lambda x: x.created_at, reverse=True)
    recent = all_transactions[:10]
    
    return DashboardResponse(
        user=UserResponse(
            id=current_user.id,
            email=current_user.email,
            name=current_user.name,
            created_at=current_user.created_at,
            is_active=current_user.is_active
        ),
        consolidated_balance=ConsolidatedBalanceResponse(
            total_brl=consolidated.total_brl,
            accounts=consolidated.accounts,
            updated_at=consolidated.updated_at
        ),
        recent_transactions=[
            TransactionResponse(
                id=tx.id,
                account_id=tx.account_id,
                type=tx.type,
                amount=tx.amount,
                currency=tx.currency,
                balance_after=tx.balance_after,
                description=tx.description,
                created_at=tx.created_at
            )
            for tx in recent
        ]
    )
