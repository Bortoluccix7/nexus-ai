
from fastapi import FastAPI

from app.core.config import settings
from app.api.routes import health


app = FastAPI(
    title=settings.APP_NAME,
    description="Plataforma de assistentes inteligentes personalizados.",
    version="0.1.0",
    debug=settings.DEBUG
)

app.include_router(
    health.router,
    prefix="/api/v1/health",
    tags=["Health"]
)
