# tests/test_transacoes.py
import pytest
from src.contas import ContaRepo
from src.transacoes import TransacaoService

def test_deposit_and_withdraw():
    cr = ContaRepo()
    c = cr.create('u1', 'BRL')
    ts = TransacaoService(cr)

    t = ts.deposit(c.id, 200.0, 'BRL')
    assert cr.get(c.id).balance == 200.0

    t2 = ts.withdraw(c.id, 50.0, 'BRL')
    assert cr.get(c.id).balance == 150.0

    with pytest.raises(ValueError):
        ts.withdraw(c.id, 1000.0, 'BRL')
