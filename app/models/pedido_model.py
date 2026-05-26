from datetime import datetime, UTC
from zoneinfo import ZoneInfo
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)
from sqlalchemy.orm import relationship
from app.banco_de_dados import Base

def agora_iso():
    return (
        datetime.now(ZoneInfo("America/Sao_Paulo"))
        .replace(microsecond=0)
        .strftime("%Y-%m-%dT%H:%M:%S")
    )

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)

    prato_principal = Column(String, nullable=False)
    acompanhamento = Column(String, nullable=False)
    observacao = Column(String)
    valor = Column(Float, nullable=False)

    restaurante_id = Column(
        Integer,
        ForeignKey("restaurantes.id"),
        nullable=False
    )

    created_at = Column(
        String,
        default=agora_iso,
    )

    updated_at = Column(
        String,
        default=agora_iso,
        onupdate=agora_iso,
    )

    restaurante = relationship(
        "Restaurante",
        back_populates="pedidos"
    )