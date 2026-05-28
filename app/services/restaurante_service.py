from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.restaurante_model import Restaurante
from app.schemas.restaurante_schema import RestauranteAlteracao, RestauranteCriacao
from app.dao.restaurante_dao import buscar_por_id, atualizar, criar, listar, deletar

def criar_restaurante(
    banco: Session,
    restaurante: RestauranteCriacao
):
    novo_restaurante = Restaurante(
        nome=restaurante.nome,
        rua=restaurante.rua,
        bairro=restaurante.bairro,
        numero=restaurante.numero,
        cidade=restaurante.cidade,
        categoria=restaurante.categoria
    )

    resturante_criado = criar(banco, novo_restaurante)
    return resturante_criado

def listar_restaurantes(banco: Session):
    restaurantes_cadastrados = listar(banco)
    return restaurantes_cadastrados

def buscar_restaurante_por_id(
    banco: Session,
    restaurante_id: int
):
    restaurante_encontrado = buscar_por_id(banco, restaurante_id)
    return restaurante_encontrado

def atualizar_restaurante(
    banco: Session,
    restaurante_id: int,
    dados_restaurante: RestauranteAlteracao
):
    restaurante_existente = buscar_restaurante_por_id(
        banco,
        restaurante_id
    )

    if not restaurante_existente:
        return None

    dados_atualizacao = dados_restaurante.model_dump(
        exclude_unset=True
    )

    restaurante_atualizado = atualizar(banco, restaurante_existente, dados_atualizacao)
    return restaurante_atualizado

def deletar_restaurante(
    banco: Session,
    restaurante_id: int
):
    restaurante = buscar_restaurante_por_id(
        banco,
        restaurante_id
    )

    if restaurante is None:
        return None

    if len(restaurante.pedidos) > 0:
        raise HTTPException(
            status_code=409,
            detail=(
                "Não é possível deletar restaurante "
                "com pedidos associados"
            )
        )

    deletar(banco, restaurante)

    return restaurante