from pydantic import BaseModel, EmailStr, model_validator

# Schema para a criação de um usuário (dados de entrada)
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    confirm_email: EmailStr
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def check_emails_match(self) -> 'UserCreate':
        if self.email != self.confirm_email:
            raise ValueError('Os e-mails não coincidem')
        return self

    @model_validator(mode='after')
    def check_passwords_match(self) -> 'UserCreate':
        if self.password != self.confirm_password:
            raise ValueError('As senhas não coincidem')
        return self

# Schema para o login de um usuário
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schema para o token JWT
class Token(BaseModel):
    access_token: str
    token_type: str

# Schema para a resposta ao criar/buscar um usuário (sem a senha)
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True