# 🏗️ Arquitetura do Orbis

## Visão Geral

```
┌─────────────────────────────────────────────┐
│              FRONTEND (React)               │
│  ┌───────────┬───────────┬────────────┐    │
│  │ Dashboard │  Accounts │Transactions│    │
│  └───────────┴───────────┴────────────┘    │
│               ↓ HTTP/REST ↓                 │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│             API (FastAPI)                   │
│  ┌──────────────────────────────────────┐  │
│  │  Routes: /auth /accounts /transactions│  │
│  │  Auth Middleware (JWT)                │  │
│  └──────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│            CORE (Domain)                    │
│  ┌──────────────────────────────────────┐  │
│  │  Services: Account, Transaction, etc  │  │
│  │  Models: User, Account, Transaction   │  │
│  │  Business Rules (Pure Python)         │  │
│  └──────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│          INFRA (Persistence)                │
│  ┌──────────────────────────────────────┐  │
│  │  Repositories: User, Account, Tx      │  │
│  │  Database Models (SQLAlchemy)         │  │
│  │  External APIs (Exchange rates)       │  │
│  └──────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
                    ↓
              ┌──────────┐
              │ SQLite   │
              │ Database │
              └──────────┘
```

## Fluxo de uma Transação

```
1. User → Frontend: Clica em "Depositar"
   ↓
2. Frontend → API: POST /api/transactions
   ↓
3. API → Auth: Valida JWT token
   ↓
4. API → Core: TransactionService.create_deposit()
   ↓
5. Core → Infra: TransactionRepository.create()
   ↓
6. Infra → DB: INSERT INTO transactions
   ↓
7. DB → Infra → Core → API → Frontend: Success!
```

## Camadas e Responsabilidades

### Frontend (Client)
- **Responsabilidade**: Interface do usuário
- **Tecnologias**: React, TailwindCSS, Axios
- **Não conhece**: Detalhes do banco de dados

### API
- **Responsabilidade**: Interface HTTP
- **Tecnologias**: FastAPI, Pydantic
- **Não contém**: Lógica de negócio

### Core
- **Responsabilidade**: Regras de negócio
- **Tecnologias**: Python puro
- **Não depende**: Framework ou banco específico

### Infra
- **Responsabilidade**: Persistência e integrações
- **Tecnologias**: SQLAlchemy, APIs externas
- **Adapta**: Core ↔ Banco de dados

## Princípios Seguidos

1. **Dependency Inversion**: Core não depende de Infra
2. **Single Responsibility**: Cada camada tem um papel
3. **Open/Closed**: Fácil adicionar novas features
4. **Separation of Concerns**: Lógica isolada da interface

## Vantagens dessa Arquitetura

✅ Fácil testar (Core isolado)
✅ Fácil trocar banco (Infra desacoplada)
✅ Fácil adicionar APIs (FastAPI modular)
✅ Código limpo e manutenível
