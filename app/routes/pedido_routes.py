from fastapi import (
    APIRouter,
    HTTPException,
    status
)

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

router_pedidos = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)

@router_pedidos.post(
    "/",
    response_model=PedidoResposta,
    status_code=status.HTTP_201_CREATED
)
def criar(
    pedido: PedidoCriacao
):
    banco = obter_banco()

    try:
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
    finally:
        banco.close()


@router_pedidos.get(
    "/",
    response_model=list[PedidoResposta]
)
def listar():
    banco = obter_banco()

    try:
        return listar_pedidos(banco)
    finally:
        banco.close()

@router_pedidos.patch(
    "/{pedido_id}",
    response_model=PedidoResposta
)
def atualizar(
    pedido_id: int,
    pedido: PedidoAlteracao
):
    banco = obter_banco()

    try:
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
    finally:
        banco.close()

@router_pedidos.delete(
    "/{pedido_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def deletar(
    pedido_id: int
):
    banco = obter_banco()

    try:
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
    finally:
        banco.close()