from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from sqlalchemy.orm import Session

from app.banco_de_dados import obter_banco
from app.schemas.restaurante_schema import (
    RestauranteAlteracao,
    RestauranteCriacao,
    RestauranteResposta,
    RestauranteEspecificoResposta
)
from app.services.restaurante_service import (
    criar_restaurante,
    listar_restaurantes,
    buscar_restaurante_por_id,
    deletar_restaurante,
    atualizar_restaurante
)

router_restaurantes = APIRouter(
    prefix="/restaurantes",
    tags=["Restaurantes"]
)

@router_restaurantes.post(
    "/",
    response_model=RestauranteResposta
)
def criar(
    restaurante: RestauranteCriacao,
    banco: Session = Depends(obter_banco)
):
    return criar_restaurante(
        banco,
        restaurante
    )

@router_restaurantes.get(
    "/",
    response_model=list[RestauranteResposta]
)
def listar(
    banco: Session = Depends(obter_banco)
):
    return listar_restaurantes(banco)

@router_restaurantes.get(
    "/{restaurante_id}",
    response_model=RestauranteEspecificoResposta
)
def buscar_por_id(
    restaurante_id: int,
    banco: Session = Depends(obter_banco)
):
    restaurante = buscar_restaurante_por_id(
        banco,
        restaurante_id
    )

    if not restaurante:

        raise HTTPException(
            status_code=404,
            detail="Restaurante não encontrado"
        )

    return restaurante

@router_restaurantes.patch(
    "/{restaurante_id}",
    response_model=RestauranteResposta
)
def atualizar(
    restaurante_id: int,
    restaurante: RestauranteAlteracao,
    banco: Session = Depends(obter_banco)
):
    restaurante_atualizado = atualizar_restaurante(
        banco,
        restaurante_id,
        restaurante
    )

    if not restaurante_atualizado:
        raise HTTPException(
            status_code=404,
            detail="Restaurante não encontrado"
        )

    return restaurante_atualizado

@router_restaurantes.delete(
    "/{restaurante_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def deletar(
    restaurante_id: int,
    banco: Session = Depends(obter_banco)
):
    restaurante = deletar_restaurante(
        banco,
        restaurante_id
    )

    if not restaurante:
        raise HTTPException(
            status_code=404,
            detail="Restaurante não encontrado"
        )

    return None