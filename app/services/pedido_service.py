from sqlalchemy.orm import Session

from app.models.pedido_model import Pedido
from app.schemas.pedido_schema import PedidoCriacao, PedidoAlteracao


def criar_pedido(
    banco: Session,
    pedido: PedidoCriacao
):
    novo_pedido = Pedido(
        prato_principal=pedido.prato_principal,
        acompanhamento=pedido.acompanhamento,
        observacao=pedido.observacao,
        valor=pedido.valor,
        restaurante_id=pedido.restaurante_id
    )

    banco.add(novo_pedido)
    banco.commit()
    banco.refresh(novo_pedido)

    return novo_pedido

def listar_pedidos(banco: Session):
    return banco.query(Pedido).all()

def buscar_pedido_por_id(
    banco: Session,
    pedido_id: int
):
    return (
        banco.query(Pedido)
        .filter(Pedido.id == pedido_id)
        .first()
    )

def atualizar_pedido(
    banco: Session,
    pedido_id: int,
    dados_pedido: PedidoAlteracao
):
    pedido = buscar_pedido_por_id(
        banco,
        pedido_id
    )

    if not pedido:
        return None

    pedido.prato_principal = dados_pedido.prato_principal
    pedido.acompanhamento = dados_pedido.acompanhamento
    pedido.observacao = dados_pedido.observacao
    pedido.valor = dados_pedido.valor
    pedido.restaurante_id = dados_pedido.restaurante_id

    banco.commit()
    banco.refresh(pedido)

    return pedido

def deletar_pedido(
    banco: Session,
    pedido_id: int
):
    pedido = buscar_pedido_por_id(
        banco,
        pedido_id
    )

    if pedido:
        banco.delete(pedido)
        banco.commit()

    return pedido