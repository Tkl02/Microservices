from pydantic import BaseModel, EmailStr, model_validator

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    confirm_email: EmailStr
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def check_email_match(self) -> 'UserCreate':
        if self.email != self.confirm_email:
            raise ValueError("Os emails não coincidem")
        return self
    
    @model_validator(mode='after')
    def check_password_match(self) -> 'UserCreate':
        if self.password != self.confirm_password:
            raise ValueError("As senhas não coincidem")
        return self

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    toke_type: str