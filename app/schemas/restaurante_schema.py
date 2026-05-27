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
        min_length=3,
        max_length=100
    )
    categoria: str = Field(
        min_length=3,
        max_length=100
    )


class RestauranteCriacao(RestauranteBase):
    pass


class RestauranteResposta(BaseModel):
    id: int
    nome: str
    rua: str
    bairro: str
    numero: int
    cidade: str
    categoria: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class RestauranteAlteracao(BaseModel):
    nome: str | None = Field(
        default=None,
        min_length=3,
        max_length=100,
        
    )
    rua: str | None = Field(
        default=None,
        min_length=3,
        max_length=255
    )
    bairro: str | None = Field(
        default=None,
        min_length=3,
        max_length=100
    )
    numero: int | None = Field(
        default=None,
        gt=0
    )
    cidade: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )
    categoria: str | None = Field(
        default=None,
        min_length=3,
        max_length=100
    )