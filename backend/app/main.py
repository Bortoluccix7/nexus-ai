
from fastapi import FastAPI

app = FastAPI(
    title="Nexus AI",
    description="Plataforma de assistentes inteligentes personalizados.",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "Nexus AI está funcionando!",
        "status": "online",
        "version": "0.1.0"
    }
