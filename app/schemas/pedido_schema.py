from datetime import datetime
from pydantic import BaseModel, Field

class PedidoBase(BaseModel):
    prato_principal: str = Field(
        min_length=1,
        max_length=255
    )
    acompanhamento: str = Field(
        min_length=1,
        max_length=255
    )
    observacao: str | None = Field(
        default=None,
        max_length=500
    )
    valor: float = Field(gt=0)
    restaurante_id: int

class PedidoCriacao(PedidoBase):
    pass

class PedidoResposta(PedidoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
