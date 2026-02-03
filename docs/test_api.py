"""
Script de teste da API - Exemplo de uso
"""
import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_flow():
    """Testa o fluxo completo do sistema"""
    
    # 1. Registrar usuário
    print("1. Registrando usuário...")
    user_data = {
        "email": "teste@orbis.com",
        "name": "Usuário Teste",
        "password": "senha123"
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
    print(f"Status: {response.status_code}")
    
    # 2. Login
    print("\n2. Fazendo login...")
    login_data = {
        "email": "teste@orbis.com",
        "password": "senha123"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    token = response.json()["access_token"]
    print(f"Token obtido: {token[:20]}...")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # 3. Criar conta em BRL
    print("\n3. Criando conta em BRL...")
    account_data = {
        "currency": "BRL",
        "label": "Conta Principal"
    }
    response = requests.post(f"{BASE_URL}/accounts/", json=account_data, headers=headers)
    account_brl = response.json()
    print(f"Conta criada: {account_brl['id']}")
    
    # 4. Criar conta em USD
    print("\n4. Criando conta em USD...")
    account_data = {
        "currency": "USD",
        "label": "Conta Dólar"
    }
    response = requests.post(f"{BASE_URL}/accounts/", json=account_data, headers=headers)
    account_usd = response.json()
    print(f"Conta criada: {account_usd['id']}")
    
    # 5. Depositar em BRL
    print("\n5. Depositando R$ 1000...")
    tx_data = {
        "account_id": account_brl["id"],
        "type": "DEPOSIT",
        "amount": 1000,
        "description": "Depósito inicial"
    }
    response = requests.post(f"{BASE_URL}/transactions/", json=tx_data, headers=headers)
    print(f"Status: {response.status_code}")
    
    # 6. Depositar em USD
    print("\n6. Depositando $ 500...")
    tx_data = {
        "account_id": account_usd["id"],
        "type": "DEPOSIT",
        "amount": 500,
        "description": "Depósito USD"
    }
    response = requests.post(f"{BASE_URL}/transactions/", json=tx_data, headers=headers)
    print(f"Status: {response.status_code}")
    
    # 7. Ver dashboard
    print("\n7. Consultando dashboard...")
    response = requests.get(f"{BASE_URL}/transactions/dashboard", headers=headers)
    dashboard = response.json()
    
    print("\n" + "="*50)
    print("DASHBOARD")
    print("="*50)
    print(f"Usuário: {dashboard['user']['name']}")
    print(f"\nSaldo Total (BRL): R$ {dashboard['consolidated_balance']['total_brl']}")
    print("\nContas:")
    for acc in dashboard['consolidated_balance']['accounts']:
        print(f"  - {acc['currency']}: {acc['balance']} (R$ {acc['balance_brl']:.2f})")
    
    print("\nTransações recentes:")
    for tx in dashboard['recent_transactions'][:5]:
        print(f"  - {tx['description']}: {tx['amount']} {tx['currency']}")

if __name__ == "__main__":
    try:
        test_flow()
    except Exception as e:
        print(f"\nErro: {e}")
