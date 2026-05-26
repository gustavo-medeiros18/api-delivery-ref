from sqlalchemy.orm import Session

from app.models.restaurante_model import Restaurante
from app.schemas.restaurante_schema import RestauranteAlteracao, RestauranteCriacao

def criar_restaurante(
    banco: Session,
    restaurante: RestauranteAlteracao
):
    novo_restaurante = Restaurante(
        nome=restaurante.nome,
        rua=restaurante.rua,
        bairro=restaurante.bairro,
        numero=restaurante.numero,
        cidade=restaurante.cidade,
        categoria=restaurante.categoria
    )

    banco.add(novo_restaurante)
    banco.commit()
    banco.refresh(novo_restaurante)

    return novo_restaurante

def listar_restaurantes(banco: Session):
    return banco.query(Restaurante).all()

def buscar_restaurante_por_id(
    banco: Session,
    restaurante_id: int
):
    return (
        banco.query(Restaurante)
        .filter(Restaurante.id == restaurante_id)
        .first()
    )

def atualizar_restaurante(
    banco: Session,
    restaurante_id: int,
    dados_restaurante: RestauranteCriacao
):
    restaurante = buscar_restaurante_por_id(
        banco,
        restaurante_id
    )

    if not restaurante:
        return None

    restaurante.nome = dados_restaurante.nome
    restaurante.rua = dados_restaurante.rua
    restaurante.bairro = dados_restaurante.bairro
    restaurante.numero = dados_restaurante.numero
    restaurante.cidade = dados_restaurante.cidade
    restaurante.categoria = dados_restaurante.categoria

    banco.commit()
    banco.refresh(restaurante)

    return restaurante

def deletar_restaurante(
    banco: Session,
    restaurante_id: int
):
    restaurante = buscar_restaurante_por_id(
        banco,
        restaurante_id
    )

    if restaurante:
        banco.delete(restaurante)
        banco.commit()

    return restaurante