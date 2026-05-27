from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.pedido_model import Pedido
from app.schemas.pedido_schema import PedidoCriacao, PedidoAlteracao
from app.services.restaurante_service import buscar_restaurante_por_id
from app.dao.pedido_dao import criar, listar, buscar_por_id, atualizar, deletar

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

    pedido_criado = criar(banco,novo_pedido)
    return pedido_criado

def listar_pedidos(banco: Session):
    pedidos_existentes = listar(banco)
    return pedidos_existentes

def buscar_pedido_por_id(
    banco: Session,
    pedido_id: int
):
    pedido_encontrado = buscar_por_id(banco, pedido_id)
    return pedido_encontrado

def atualizar_pedido(
    banco: Session,
    pedido_id: int,
    dados_pedido: PedidoAlteracao
):
    pedido_existente = buscar_pedido_por_id(
        banco,
        pedido_id
    )

    if not pedido_existente:
        return None

    if dados_pedido.restaurante_id != None:
        restaurante = buscar_restaurante_por_id(
            banco,
            dados_pedido.restaurante_id
        )

        if not restaurante:
            raise HTTPException(
                status_code=404,
                detail="Restaurante não encontrado"
            )

    dados_atualizacao = dados_pedido.model_dump(
        exclude_unset=True
    )

    pedido_atualizado = atualizar(banco, pedido_existente, dados_atualizacao)
    return pedido_atualizado

def deletar_pedido(
    banco: Session,
    pedido_id: int
):
    pedido_existente = buscar_pedido_por_id(
        banco,
        pedido_id
    )

    if pedido_existente != None:
        deletar(banco, pedido_existente)

    return pedido_existente