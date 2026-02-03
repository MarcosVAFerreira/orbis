"""
Serviços de domínio - Regras de negócio do Orbis
"""
from decimal import Decimal
from typing import List, Optional
from datetime import datetime

from .models import (
    Account, Transaction, TransactionType, 
    Currency, ConsolidatedBalance, AccountStatus
)


class AccountService:
    """Serviço de gerenciamento de contas"""
    
    @staticmethod
    def create_account(user_id: str, currency: Currency, label: str = "") -> Account:
        """Cria uma nova conta"""
        return Account(
            user_id=user_id,
            currency=currency,
            label=label or f"Conta {currency.value}"
        )
    
    @staticmethod
    def can_transact(account: Account) -> bool:
        """Verifica se a conta pode realizar transações"""
        return account.status == AccountStatus.ACTIVE


class TransactionService:
    """Serviço de transações - núcleo do sistema"""
    
    @staticmethod
    def calculate_balance(transactions: List[Transaction]) -> Decimal:
        """Calcula saldo a partir do ledger"""
        balance = Decimal("0")
        for tx in transactions:
            if tx.type in [TransactionType.DEPOSIT, TransactionType.TRANSFER]:
                balance += tx.amount
            elif tx.type == TransactionType.WITHDRAWAL:
                balance -= tx.amount
        return balance
    
    @staticmethod
    def create_deposit(
        account_id: str, 
        amount: Decimal, 
        currency: Currency,
        description: str = ""
    ) -> Transaction:
        """Cria um depósito"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        return Transaction(
            account_id=account_id,
            type=TransactionType.DEPOSIT,
            amount=amount,
            currency=currency,
            description=description or "Depósito"
        )
    
    @staticmethod
    def create_withdrawal(
        account_id: str,
        amount: Decimal,
        currency: Currency,
        current_balance: Decimal,
        description: str = ""
    ) -> Transaction:
        """Cria um saque"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > current_balance:
            raise ValueError("Insufficient funds")
        
        return Transaction(
            account_id=account_id,
            type=TransactionType.WITHDRAWAL,
            amount=amount,
            currency=currency,
            description=description or "Saque"
        )


class ExchangeService:
    """Serviço de câmbio"""
    
    # Taxas mockadas para o protótipo
    RATES = {
        Currency.BRL: Decimal("1.0"),
        Currency.USD: Decimal("5.20"),
        Currency.EUR: Decimal("5.65"),
        Currency.GBP: Decimal("6.50"),
        Currency.JPY: Decimal("0.035"),
    }
    
    @classmethod
    def get_rate(cls, from_currency: Currency, to_currency: Currency = Currency.BRL) -> Decimal:
        """Obtém taxa de conversão"""
        if from_currency == to_currency:
            return Decimal("1.0")
        
        # Converte tudo para BRL como base
        from_rate = cls.RATES.get(from_currency, Decimal("1.0"))
        to_rate = cls.RATES.get(to_currency, Decimal("1.0"))
        
        return from_rate / to_rate
    
    @classmethod
    def convert(cls, amount: Decimal, from_currency: Currency, to_currency: Currency) -> Decimal:
        """Converte valor entre moedas"""
        rate = cls.get_rate(from_currency, to_currency)
        return amount * rate


class ConsolidationService:
    """Serviço de consolidação de saldos"""
    
    @staticmethod
    def consolidate_balance(accounts_data: List[dict]) -> ConsolidatedBalance:
        """
        Consolida saldos de todas as contas em BRL
        accounts_data: [{"currency": "USD", "balance": 100}, ...]
        """
        total_brl = Decimal("0")
        account_details = []
        
        for acc in accounts_data:
            currency = acc["currency"]
            balance = Decimal(str(acc["balance"]))
            
            balance_brl = ExchangeService.convert(balance, currency, Currency.BRL)
            total_brl += balance_brl
            
            account_details.append({
                "currency": currency.value,
                "balance": float(balance),
                "balance_brl": float(balance_brl),
                "rate": float(ExchangeService.get_rate(currency))
            })
        
        return ConsolidatedBalance(
            total_brl=total_brl,
            accounts=account_details,
            updated_at=datetime.utcnow()
        )
