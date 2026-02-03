"""
Rotas de autenticação
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import UserRegister, UserLogin, Token, UserResponse
from ..auth import hash_password, verify_password, create_access_token, get_current_user
from core.models import User
from infra.repositories import UserRepository

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserRegister, db: Session = Depends(get_db)):
    """Registra um novo usuário"""
    user_repo = UserRepository(db)
    
    # Verifica se email já existe
    existing_user = user_repo.get_by_email(user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Cria usuário
    user = User(
        email=user_data.email,
        name=user_data.name,
        password_hash=hash_password(user_data.password)
    )
    
    created_user = user_repo.create(user)
    
    return UserResponse(
        id=created_user.id,
        email=created_user.email,
        name=created_user.name,
        created_at=created_user.created_at,
        is_active=created_user.is_active
    )


@router.post("/login", response_model=Token)
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    """Autentica um usuário"""
    user_repo = UserRepository(db)
    user = user_repo.get_by_email(credentials.email)
    
    if not user or not verify_password(credentials.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    access_token = create_access_token(data={"sub": user.id})
    
    return Token(access_token=access_token)


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    """Retorna dados do usuário autenticado"""
    return UserResponse(
        id=current_user.id,
        email=current_user.email,
        name=current_user.name,
        created_at=current_user.created_at,
        is_active=current_user.is_active
    )
