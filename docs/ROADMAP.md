# 🚀 Roadmap de Features - Orbis

## ✅ Implementado (Protótipo)

- [x] Autenticação JWT
- [x] CRUD de usuários
- [x] CRUD de contas multi-moeda
- [x] Transações (depósito/saque)
- [x] Consolidação de saldo
- [x] Dashboard web
- [x] Histórico de transações

## 🎯 Próximas Features (por prioridade)

### Sprint 1: Fundamentos

**1. Testes Automatizados**
```python
# tests/test_transaction_service.py
def test_deposit_increases_balance():
    service = TransactionService()
    # ...
```

**2. Validações Robustas**
- Limites de transação
- Verificação de saldo
- Validação de moedas

**3. Tratamento de Erros**
- Exceções customizadas
- Logs estruturados
- Mensagens claras

### Sprint 2: Melhorias de UX

**1. Conversão de Moedas**
```python
# Converter entre contas
POST /api/transactions/convert
{
    "from_account_id": "...",
    "to_account_id": "...",
    "amount": 100
}
```

**2. Filtros e Busca**
- Filtrar por data
- Buscar por descrição
- Exportar relatórios

**3. Notificações**
- Toast messages
- Confirmações
- Alertas de erro

### Sprint 3: Features Avançadas

**1. Transferências**
```python
# Entre contas do mesmo usuário
POST /api/transactions/transfer
{
    "from_account_id": "...",
    "to_account_id": "...",
    "amount": 100
}
```

**2. Agendamento**
- Transações recorrentes
- Agendamento futuro
- Lembretes

**3. Relatórios**
- Gráficos de gastos
- Análise por categoria
- Exportação PDF

### Sprint 4: Infraestrutura

**1. Cache com Redis**
```python
# Cachear taxas de câmbio
@cache.cached(timeout=3600)
def get_exchange_rates():
    # ...
```

**2. PostgreSQL**
```python
# Migração do SQLite
DATABASE_URL=postgresql://user:pass@localhost/orbis
```

**3. API Externa Real**
```python
# Integração com API de câmbio
import requests
rates = requests.get("https://api.exchangerate.host/latest")
```

### Sprint 5: Segurança

**1. Rate Limiting**
```python
from slowapi import Limiter
limiter = Limiter(key_func=get_remote_address)

@app.post("/login")
@limiter.limit("5/minute")
def login():
    # ...
```

**2. 2FA (Two-Factor Auth)**
- TOTP (Google Authenticator)
- SMS
- Email

**3. Auditoria**
```python
# Log todas as ações críticas
class AuditLog:
    user_id: str
    action: str
    timestamp: datetime
    ip_address: str
```

### Sprint 6: Produção

**1. CI/CD**
```yaml
# .github/workflows/deploy.yml
name: Deploy
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    # ...
```

**2. Monitoramento**
- Sentry (erros)
- Prometheus (métricas)
- Grafana (dashboards)

**3. Backup**
- Backup automático
- Replicação
- Disaster recovery

## 💡 Ideas (Futuro Distante)

### Mobile App
```
React Native / Flutter
- Notificações push
- Biometria
- Modo offline
```

### Integrações
- Open Banking
- PIX
- Boletos
- Cartões virtuais

### Machine Learning
- Detecção de fraude
- Categorização automática
- Previsão de gastos
- Insights personalizados

### Gamificação
- Metas de economia
- Conquistas
- Ranking de amigos
- Desafios

## 📝 Como Implementar

### Exemplo: Adicionar Transferências

1. **Core (Domain)**
```python
# core/services.py
@staticmethod
def create_transfer(
    from_account_id: str,
    to_account_id: str,
    amount: Decimal
) -> Tuple[Transaction, Transaction]:
    # Validações
    # Criar duas transações
    # Retornar ambas
```

2. **API (Routes)**
```python
# api/routes/transactions.py
@router.post("/transfer")
def transfer(data: TransferCreate):
    # Validar contas
    # Chamar serviço
    # Retornar resultado
```

3. **Frontend**
```javascript
// src/pages/Transfer.jsx
function Transfer() {
    // Form de transferência
    // Validações
    // Chamada API
}
```

## 🎓 Aprenda Fazendo

Escolha uma feature acima e implemente-a! O código está estruturado para facilitar extensões.

Dica: Comece pelas features mais simples (testes, validações) antes de partir para as complexas (ML, integrações).
