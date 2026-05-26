from datetime import datetime, UTC
from zoneinfo import ZoneInfo
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.banco_de_dados import Base

def agora_iso():
    return (
        datetime.now(ZoneInfo("America/Sao_Paulo"))
        .replace(microsecond=0)
        .strftime("%Y-%m-%dT%H:%M:%S")
    )

class Restaurante(Base):
    __tablename__ = "restaurantes"
    
    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String, nullable=False)
    rua = Column(String, nullable=False)
    bairro = Column(String, nullable=False)
    numero = Column(Integer, nullable=False)
    cidade = Column(String, nullable=False)
    categoria = Column(String, nullable=False)

    created_at = Column(
        String,
        default=agora_iso,
    )

    updated_at = Column(
        String,
        default=agora_iso,
        onupdate=agora_iso
    )

    pedidos = relationship(
        "Pedido",
        back_populates="restaurante"
    )
