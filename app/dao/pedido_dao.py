from sqlalchemy.orm import Session

from app.models.pedido_model import Pedido

def criar(
    banco: Session,
    novo_pedido: Pedido
):
    banco.add(novo_pedido)
    banco.commit()
    banco.refresh(novo_pedido)

    return novo_pedido

def listar(banco: Session):
    return banco.query(Pedido).all()

def buscar_por_id(
    banco: Session,
    pedido_id: int
):
    return (
        banco.query(Pedido)
        .filter(Pedido.id == pedido_id)
        .first()
    )

def atualizar(
    banco: Session,
    pedido: Pedido,
    dados_atualizacao: dict
):
    for campo, valor in dados_atualizacao.items():
        setattr(pedido, campo, valor)

    banco.commit()
    banco.refresh(pedido)

    return pedido

def deletar(
    banco: Session,
    pedido: Pedido
):
    banco.delete(pedido)
    banco.commit()