# 🌐 Orbis - Sistema Bancário Multicurrency

> Plataforma bancária modular, orientada a API, com foco educacional e arquitetural

## 🚀 Quick Start

### Backend
```bash
cd api
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd client
npm install
npm run dev
```

### Docker (Recomendado)
```bash
docker-compose up
```

## 📁 Estrutura

```
Orbis/
├── api/          # FastAPI - Interface HTTP
├── core/         # Domínio e regras de negócio
├── infra/        # Banco, cache, APIs externas
├── client/       # React - Interface Web
├── tests/        # Testes automatizados
└── docs/         # Documentação
```

## 🔑 Features Implementadas (Protótipo)

- ✅ Autenticação JWT
- ✅ Gerenciamento de usuários
- ✅ Contas multi-moeda
- ✅ Transações (depósito, saque, transferência)
- ✅ Conversão de moedas em tempo real
- ✅ Dashboard consolidado
- ✅ Histórico de transações

## 🛠 Stack Técnica

**Backend:**
- FastAPI
- SQLAlchemy 2.0
- SQLite (dev) / PostgreSQL (prod)
- JWT + bcrypt
- Pydantic

**Frontend:**
- React + Vite
- TailwindCSS
- Axios
- React Router

## 📊 API Endpoints

Acesse `http://localhost:8000/docs` para a documentação interativa (Swagger)

## 🧪 Testes

```bash
pytest tests/
```

## 📝 Licença

MIT - Projeto educacional
