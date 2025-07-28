from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

import crud
import models
import schemas
import database

# Cria as tabelas no banco de dados
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Serviço de Usuários")

@app.get("/", summary="Health Check", tags=["Root"])
def read_root():
    return {"service": "users-service", "status": "OK"}

@app.post("/auth/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED, summary="Registrar um novo usuário", tags=["Auth"])
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já registrado"
        )
    
    new_user = crud.create_user(db=db, user=user)
    return new_user

@app.post("/auth/login", status_code=status.HTTP_200_OK, summary="Fazer login", tags=["Auth"])
def login_user(user_data: schemas.UserLogin, db: Session = Depends(database.get_db)):
    # Lógica do login será implementada no próximo passo
    return {"access_token": "placeholder_for_real_jwt", "token_type": "bearer"}