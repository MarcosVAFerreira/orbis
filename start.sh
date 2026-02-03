#!/bin/bash

echo "🌐 Orbis - Quick Start"
echo "======================"
echo ""

# Verifica se Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Docker não encontrado. Instalando manualmente..."
    echo ""
    
    # Backend
    echo "📦 Instalando backend..."
    cd api
    pip install -r requirements.txt
    cd ..
    
    # Frontend
    echo "📦 Instalando frontend..."
    cd client
    npm install
    cd ..
    
    echo ""
    echo "✅ Instalação concluída!"
    echo ""
    echo "Para iniciar:"
    echo "  Backend:  cd api && uvicorn main:app --reload"
    echo "  Frontend: cd client && npm run dev"
else
    echo "✅ Docker encontrado! Usando Docker Compose..."
    echo ""
    docker-compose up -d
    
    echo ""
    echo "✅ Serviços iniciados!"
    echo ""
    echo "  🔗 API:      http://localhost:8000"
    echo "  📚 Docs:     http://localhost:8000/docs"
    echo "  🌐 Frontend: http://localhost:5173"
fi

echo ""
echo "📖 Leia docs/DEVELOPMENT.md para mais informações"
