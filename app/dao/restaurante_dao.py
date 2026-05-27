from sqlalchemy.orm import Session

from app.models.restaurante_model import Restaurante

def criar(
    banco: Session,
    novo_restaurante: Restaurante
):
    banco.add(novo_restaurante)
    banco.commit()
    banco.refresh(novo_restaurante)

    return novo_restaurante

def listar(banco: Session):
    return banco.query(Restaurante).all()

def buscar_por_id(
    banco: Session,
    restaurante_id: int
):
    return (
        banco.query(Restaurante)
        .filter(Restaurante.id == restaurante_id)
        .first()
    )

def atualizar(
    banco: Session,
    restaurante: Restaurante,
    dados_atualizacao: dict
):
    for campo, valor in dados_atualizacao.items():
        setattr(restaurante, campo, valor)

    banco.commit()
    banco.refresh(restaurante)

    return restaurante

def deletar(
    banco: Session,
    restaurante: Restaurante
):
    banco.delete(restaurante)
    banco.commit()