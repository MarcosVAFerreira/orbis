# 🎯 LEIA PRIMEIRO - Orbis Protótipo

## O que você recebeu

Um **protótipo completo e funcional** do Orbis com:

✅ **Backend FastAPI** - API REST completa com autenticação JWT
✅ **Frontend React** - Interface web moderna e responsiva  
✅ **Arquitetura Limpa** - Separação clara entre domínio, API e infraestrutura
✅ **Banco de Dados** - SQLite (dev) com modelos prontos
✅ **Docker** - Containerização completa do projeto

## Como começar AGORA

### Opção 1: Docker (Mais Rápido)
```bash
docker-compose up
```

### Opção 2: Manual
```bash
# Terminal 1 - Backend
cd api
pip install -r requirements.txt
uvicorn main:app --reload

# Terminal 2 - Frontend
cd client
npm install
npm run dev
```

Acesse: http://localhost:5173

## Primeiro uso

1. Clique em "Registrar"
2. Crie sua conta
3. Crie contas em diferentes moedas (BRL, USD, EUR...)
4. Faça depósitos e saques
5. Veja o saldo consolidado no dashboard

## Estrutura do código

```
orbis/
├── api/          ← FastAPI (rotas HTTP)
├── core/         ← Lógica de negócio
├── infra/        ← Banco de dados
├── client/       ← React (interface)
└── docs/         ← Documentação
```

## Arquivos importantes

- `README.md` - Visão geral do projeto
- `docs/DEVELOPMENT.md` - Guia de desenvolvimento
- `docs/ARCHITECTURE.md` - Como funciona a arquitetura
- `docs/ROADMAP.md` - Próximas features para implementar
- `docs/test_api.py` - Script para testar a API

## O que estudar primeiro

### Se você quer entender o BACKEND:
1. Leia `core/models.py` - Entidades do domínio
2. Leia `core/services.py` - Regras de negócio
3. Leia `api/routes/` - Endpoints REST
4. Experimente modificar limites de transação

### Se você quer entender o FRONTEND:
1. Leia `client/src/App.jsx` - Estrutura principal
2. Leia `client/src/pages/Dashboard.jsx` - Tela principal
3. Leia `client/src/services/api.js` - Cliente HTTP
4. Experimente mudar cores e layout

### Se você quer adicionar features:
1. Leia `docs/ROADMAP.md` - Lista de próximas features
2. Escolha uma feature simples (ex: filtros)
3. Implemente seguindo a arquitetura existente
4. Teste e itere

## Features implementadas

✅ Autenticação e registro de usuários
✅ Criação de contas multi-moeda (BRL, USD, EUR, GBP, JPY)
✅ Depósitos e saques
✅ Consolidação automática de saldo em BRL
✅ Histórico de transações
✅ Dashboard com visão geral
✅ Validações e tratamento de erros
✅ JWT para autenticação
✅ API documentada (Swagger)

## Próximos passos sugeridos

1. **Rode o projeto** e teste todas as funcionalidades
2. **Leia o código** começando pelo README de cada pasta
3. **Faça pequenas modificações** para entender o fluxo
4. **Adicione testes** para as funcionalidades existentes
5. **Implemente uma nova feature** do ROADMAP

## Tecnologias usadas

**Backend:**
- Python 3.12
- FastAPI (API REST)
- SQLAlchemy (ORM)
- JWT (Autenticação)
- Pydantic (Validação)

**Frontend:**
- React 18
- Vite (Build tool)
- TailwindCSS (Styling)
- React Router (Navegação)
- Axios (HTTP)

**Infra:**
- Docker & Docker Compose
- SQLite (desenvolvimento)

## Precisa de ajuda?

- 📚 Documentação completa em `docs/`
- 🐛 Problemas? Verifique os logs do terminal
- 💡 Ideias? Veja `docs/ROADMAP.md`
- 🧪 Teste a API: `python docs/test_api.py`

## Este é um projeto educacional

O Orbis foi feito para:
- ✅ Aprender arquitetura limpa
- ✅ Praticar FastAPI e React
- ✅ Entender sistemas bancários
- ✅ Construir um portfólio sólido

**Não é para produção sem melhorias de segurança!**

---

**Dica final:** Não tente entender tudo de uma vez. Comece rodando o projeto, depois explore o código aos poucos. Boa sorte! 🚀
