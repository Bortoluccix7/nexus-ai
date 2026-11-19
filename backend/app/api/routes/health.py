
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def health_check():
    return {
        "status": "online",
        "message": "Nexus AI API is running!"
    }
