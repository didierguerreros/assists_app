from pydantic import BaseModel
from enum import Enum

class Role(str, Enum):
    docente = "docente"
    coordinador = "coordinador"
    admin = "admin"

class UsuarioCreate(BaseModel):
    username: str
    password: str
    role: Role

class UsuarioResponse(BaseModel):
    id: int
    username: str
    role: Role

    class Config:
        orm_mode = True
