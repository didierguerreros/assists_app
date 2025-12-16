from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth import authenticate_user, create_access_token
from app.schemas.usuario import UsuarioCreate
from app.models.usuario import Usuario

router = APIRouter(prefix="/auth", tags=["Autenticación"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    user = authenticate_user(usuario.username, usuario.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    # Crear token
    access_token = create_access_token(data={"sub": user.username, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}
