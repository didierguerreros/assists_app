from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
from enum import Enum as PyEnum

class Role(PyEnum):
    docente = "docente"
    coordinador = "coordinador"
    admin = "admin"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(Role), default=Role.docente)