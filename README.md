# 🌐 Orbis — Sistema Bancário em Python
## 🔗 Demonstração Online
Acesse a versão web diretamente no navegador (funciona em PC, celular e tablet, sem downloads):
👉 https://MarcosVAFerreira.github.io/orbis

# 🧭 Visão Geral
Orbis é um sistema bancário modular desenvolvido em Python, com foco em:
Controle financeiro simples e transparente
Segurança e consistência de operações
Suporte a múltiplas moedas
Expansão futura para integração com APIs reais de câmbio
Execução tanto localmente quanto no navegador via GitHub Pages
O objetivo é criar uma experiência inspirada no Wise, onde o usuário vê seu saldo consolidado em reais mesmo operando com moedas diferentes.

# ⚙️ Funcionalidades
✔️ Funcionais
Criar e gerenciar usuários
Criar contas bancárias
Depósito com validação
Saque com limite e verificação de saldo
Extrato detalhado por conta
Conversão automática de moedas

# 🚧 Em desenvolvimento
API completa (Flask)
Integração com React
Backend real usando PostgreSQL
Autenticação e autorização

# 🧩 Stack Técnica
Camada	Tecnologias
Linguagem	Python 3.12
Backend	Flask (API REST – WIP)
Frontend Web	HTML, CSS, JavaScript
Banco de dados (planejado)	PostgreSQL
Ferramentas	VSCode, GitHub Pages, Docker, Obsidian

### 🗂️ Estrutura do Projeto
Orbis/
├── api/               # Endpoints Flask (em desenvolvimento)
├── client/            # Interface web estática (HTML/CSS/JS) – usada no GitHub Pages
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── src/
│   ├── core/          # Lógica principal (contas, usuários, transações)
│   ├── utils/         # Funções auxiliares
│   ├── data/          # Banco de dados em memória
│   └── __init__.py
├── tests/             # Testes unitários (pytest)
├── docs/              # Página publicada pelo GitHub Pages
├── requirements.txt
├── .gitignore
└── README.md

# 🚀 Como Executar Localmente
## 1️⃣ Clonar o repositório
git clone https://github.com/MarcosVAFerreira/orbis.git
cd orbis
## 2️⃣ Criar ambiente virtual
python -m venv venv
### Ativar o ambiente
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows

## 3️⃣ Instalar dependências
pip install -r requirements.txt

## 4️⃣ Executar a versão Python
python src/core/main.py

# 🌐 Como Acessar a Versão Web
A versão web funciona pelo GitHub Pages e pode ser acessada em:
👉 https://MarcosVAFerreira.github.io/orbis
A interface web está na pasta /client e é copiada automaticamente para /docs no branch main, garantindo publicação automática.

# 📜 Licença
Distribuído sob a licença MIT — livre para usar, modificar e contribuir.
