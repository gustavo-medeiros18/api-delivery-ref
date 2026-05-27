from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from sqlalchemy.orm import Session

from app.banco_de_dados import obter_banco
from app.schemas.pedido_schema import (
    PedidoCriacao,
    PedidoResposta,
    PedidoAlteracao
)
from app.services.pedido_service import (
    criar_pedido,
    listar_pedidos,
    buscar_pedido_por_id,
    deletar_pedido,
    atualizar_pedido
)
from app.services.restaurante_service import (
    buscar_restaurante_por_id
)

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)

@router.post(
    "/",
    response_model=PedidoResposta
)
def criar(
    pedido: PedidoCriacao,
    banco: Session = Depends(obter_banco)
):
    restaurante = buscar_restaurante_por_id(
        banco,
        pedido.restaurante_id
    )

    if not restaurante:
        raise HTTPException(
            status_code=404,
            detail="Restaurante não encontrado"
        )

    return criar_pedido(
        banco,
        pedido
    )


@router.get(
    "/",
    response_model=list[PedidoResposta]
)
def listar(
    banco: Session = Depends(obter_banco)
):
    return listar_pedidos(banco)


@router.get(
    "/{pedido_id}",
    response_model=PedidoResposta
)
def buscar_por_id(
    pedido_id: int,
    banco: Session = Depends(obter_banco)
):
    pedido = buscar_pedido_por_id(
        banco,
        pedido_id
    )

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado"
        )

    return pedido

@router.patch(
    "/{pedido_id}",
    response_model=PedidoResposta
)
def atualizar(
    pedido_id: int,
    pedido: PedidoAlteracao,
    banco: Session = Depends(obter_banco)
):
    pedido_atualizado = atualizar_pedido(
        banco,
        pedido_id,
        pedido
    )

    if not pedido_atualizado:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado"
        )

    return pedido_atualizado

@router.delete(
    "/{pedido_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def deletar(
    pedido_id: int,
    banco: Session = Depends(obter_banco)
):
    pedido = deletar_pedido(
        banco,
        pedido_id
    )

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado"
        )

    return None