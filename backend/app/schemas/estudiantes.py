from pydantic import BaseModel

class EstudianteCreate(BaseModel):
    nombre: str
    curso: str

class EstudianteResponse(EstudianteCreate):
    id: int

    class Config:
        from_attributes = True
