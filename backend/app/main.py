from fastapi import FastAPI
from app.routers import estudiantes, auth  # No uses 'backend' aquí

app = FastAPI()

# Registrar los routers
app.include_router(estudiantes.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "API de inasistencias activa"}