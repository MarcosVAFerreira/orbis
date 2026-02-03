"""
Configuração de banco de dados
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

# Adiciona os diretórios ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from infra.database import Base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./orbis.db")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Dependency para obter sessão de BD"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
