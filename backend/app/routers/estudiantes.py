from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from backend.app.models.estudiantes import Estudiante
from backend.app.schemas.estudiantes import EstudianteCreate, EstudianteResponse
from app.database import Base

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EstudianteResponse)
def crear_estudiante(estudiante: EstudianteCreate, db: Session = Depends(get_db)):
    nuevo = Estudiante(**estudiante.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=list[EstudianteResponse])
def listar_estudiantes(db: Session = Depends(get_db)):
    return db.query(Estudiante).all()
