from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class RestauranteBase(BaseModel):
    nome: str = Field(
        min_length=3,
        max_length=100
    )
    rua: str = Field(
        min_length=3,
        max_length=255
    )
    bairro: str = Field(
        min_length=3,
        max_length=100
    )
    numero: int = Field(
        gt=0
    )
    cidade: str = Field(
        min_length=2,
        max_length=100
    )
    categoria: str = Field(
        min_length=3,
        max_length=100
    )


class RestauranteCriacao(RestauranteBase):
    pass


class RestauranteResposta(RestauranteBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )