# 📖 Guia de Desenvolvimento - Orbis

## 🎯 Você está aqui

Este é um **protótipo funcional completo** do Orbis com backend FastAPI e frontend React.

## 🚀 Como rodar

### Opção 1: Docker (Recomendado)

```bash
# Na raiz do projeto
docker-compose up
```

- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- Frontend: http://localhost:5173

### Opção 2: Manual

**Backend:**
```bash
cd api
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend:**
```bash
cd client
npm install
npm run dev
```

## 🧪 Testando o sistema

1. Acesse http://localhost:5173
2. Crie uma conta (Register)
3. Faça login
4. Crie contas em diferentes moedas
5. Realize depósitos e saques
6. Veja o saldo consolidado no dashboard

## 📚 Próximos passos para estudar

### Backend (FastAPI)

1. **Entenda a arquitetura:**
   - `core/` - Regras de negócio puras
   - `infra/` - Acesso a dados
   - `api/` - Interface HTTP

2. **Estude:**
   - `core/services.py` - Lógica de negócio
   - `api/routes/` - Endpoints REST
   - `api/auth.py` - Autenticação JWT

3. **Experimente:**
   - Adicionar novas moedas
   - Criar transferências entre contas
   - Implementar limites de transação

### Frontend (React)

1. **Explore:**
   - `src/pages/` - Páginas da aplicação
   - `src/services/api.js` - Cliente HTTP
   - `src/components/` - Componentes reutilizáveis

2. **Melhore:**
   - Adicionar gráficos (Chart.js)
   - Melhorar validações de formulário
   - Adicionar notificações toast

## 🔧 Melhorias sugeridas

### Curto prazo
- [ ] Adicionar testes unitários
- [ ] Implementar paginação nas transações
- [ ] Adicionar filtros de data
- [ ] Melhorar tratamento de erros

### Médio prazo
- [ ] Cache de taxas de câmbio
- [ ] API externa real de câmbio
- [ ] Transferências entre contas
- [ ] Gráficos e relatórios

### Longo prazo
- [ ] Migrar para PostgreSQL
- [ ] Implementar Redis para cache
- [ ] Adicionar webhooks
- [ ] Sistema de notificações

## 📖 Documentação API

Acesse http://localhost:8000/docs para ver a documentação interativa (Swagger).

## 🐛 Debugando

**Backend:**
```python
# Adicione logs
import logging
logging.basicConfig(level=logging.DEBUG)
```

**Frontend:**
```javascript
// Console do navegador
console.log('Debug:', data)
```

## 📝 Notas importantes

- O banco SQLite é criado automaticamente em `api/orbis.db`
- Tokens JWT expiram em 24 horas
- Senhas são hasheadas com bcrypt
- CORS está configurado para desenvolvimento

## 🤝 Contribuindo

Este é um projeto educacional. Sinta-se livre para:
- Experimentar novas features
- Refatorar código
- Adicionar testes
- Melhorar a UI/UX

## 📚 Recursos

- [FastAPI Docs](https://fastapi.tiangolo.com)
- [React Docs](https://react.dev)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org)
- [Tailwind CSS](https://tailwindcss.com)
