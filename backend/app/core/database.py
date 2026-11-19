
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.core.config import settings


# Conexão com o PostgreSQL
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG
)


# Gerenciador de sessões
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# Classe base dos nossos modelos
class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()