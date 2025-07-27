import schemas
from fastapi import FastAPI

app = FastAPI(title="Serviço de usuarios")

@app.get("/", summary="health Check", tags=["Root"])
def read_root():
    """
    End point raiz para verificar se o serviço esta no ar.
    """
    return{"service":"user-service", "status":"OK"}

@app.post("/auth/register", status_code=201, summary="registrar um novo usuario", tags=["Auth"])
def register_user(user: schemas.UserCreate):
    """
        Endpoint para registrar um novo usuario.
    """
    return {"message":"Usuario registrado com sucesso","user": user.username}

@app.post("/auth/login",status_code=200, summary="login do usuario", tags=["Auth"])
def login_user(user_data: schemas.UserLogin):
    """
    Endpoit para fazer o login do usuario
    """
    return{"access_token":"fake-jwt-token" + user_data.email, "token_type":"bearer"}