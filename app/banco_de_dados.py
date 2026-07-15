from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

URL_BANCO = "sqlite:///./delivery.db"

engine = create_engine(
    URL_BANCO
)

SessaoLocal = sessionmaker(
    bind=engine
)

Base = declarative_base()

def obter_banco():
    banco = SessaoLocal()

    return banco