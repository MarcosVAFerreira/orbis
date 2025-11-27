# 🌐 Orbis — Sistema Bancário em Python
## 🌐 Demonstração Online

Acesse a versão web do Orbis diretamente pelo navegador:

👉 **https://MarcosVAFerreira.github.io/orbis**

> Funciona em navegador, celular e PC — sem precisar baixar o repositório.

[![Status](https://img.shields.io/badge/status-em_desenvolvimento-yellow)](#)
[![Python](https://img.shields.io/badge/python-3.12+-blue)](#)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Made with ❤️ by Marcos Ferreira](https://img.shields.io/badge/made%20with-❤️%20by%20Marcos%20Ferreira-blueviolet)](#)

---

## 🧭 Visão Geral
**Orbis** é um sistema bancário inteligente, desenvolvido em **Python**, com foco em controle financeiro, segurança e integração multi-moeda.  
A proposta é oferecer uma experiência semelhante ao **Wise**, convertendo automaticamente valores de diferentes moedas para o total em reais — sem necessidade de transferências entre contas locais.

---

## ⚙️ Funcionalidades

✅ Criação de contas e usuários  
✅ Depósito, saque e extrato detalhado  
✅ Controle de saldo e limites de saque  
✅ Conversão automática de moedas (multi-moeda)  
🚧 Integração futura com APIs de câmbio  
🚧 Interface web (Flask + React)

---

## 🧩 Stack Técnica

| Categoria | Ferramentas |
|------------|--------------|
| **Linguagem** | Python 3.12 |
| **Frameworks (futuro)** | Flask (API), React (frontend), Bootstrap |
| **Banco de dados** | PostgreSQL |
| **Ferramentas utilizadas** | VSCode, Docker, Git, Obsidian |

---

## 🧱 Estrutura do Projeto
```
Orbis/
├── src/
│ ├── core/ # Lógica principal do sistema (usuários, contas, transações)
│ ├── utils/ # Funções auxiliares, logs e validações
│ ├── api/ # Interface Flask (futuro)
│ └── init.py
├── tests/ # Testes unitários e de integração
├── requirements.txt
├── .gitignore
└── README.md
````


## 🚀 Como Executar Localmente

```bash
# 1️⃣ Clonar o repositório
git clone https://github.com/MarcosVAFerreira/orbis.git
cd orbis

# 2️⃣ Criar ambiente virtual
python -m venv venv
source venv/bin/activate   # (Linux/macOS)
venv\Scripts\activate      # (Windows)

# 3️⃣ Instalar dependências
pip install -r requirements.txt

# 4️⃣ Executar o sistema
python src/core/main.py


