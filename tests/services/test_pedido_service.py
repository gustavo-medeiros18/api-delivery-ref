from unittest.mock import patch, MagicMock

from fastapi import HTTPException
import pytest

from app.services.pedido_service import (
    atualizar_pedido,
    criar_pedido,
    buscar_pedido_por_id,
    deletar_pedido
)
from app.schemas.pedido_schema import (
    PedidoAlteracao,
    PedidoCriacao
)

@patch("app.services.pedido_service.criar")
def test_criar_pedido(
    mock_criar
):
    banco_mock = MagicMock()

    pedido_schema = PedidoCriacao(
        prato_principal="Hamburguer",
        acompanhamento="Batata",
        observacao="Sem cebola",
        valor=30.0,
        restaurante_id=1
    )

    mock_criar.return_value = {
        "id": 1,
        "prato_principal": "Hamburguer"
    }

    resultado = criar_pedido(
        banco_mock,
        pedido_schema
    )

    mock_criar.assert_called_once()

    assert resultado["id"] == 1

@patch("app.services.pedido_service.buscar_por_id")
def test_buscar_pedido_por_id(
    mock_buscar
):
    banco_mock = MagicMock()

    mock_buscar.return_value = {
        "id": 1,
        "prato_principal": "Pizza"
    }

    resultado = buscar_pedido_por_id(
        banco_mock,
        1
    )

    assert resultado["prato_principal"] == "Pizza"

@patch("app.services.pedido_service.buscar_pedido_por_id")
def test_atualizar_pedido_retorna_none_quando_pedido_nao_existe(
    mock_buscar_pedido
):
    banco_mock = MagicMock()

    mock_buscar_pedido.return_value = None

    dados = PedidoAlteracao(
        valor=50
    )

    resultado = atualizar_pedido(
        banco_mock,
        1,
        dados
    )

    assert resultado is None


@patch("app.services.pedido_service.buscar_restaurante_por_id")
@patch("app.services.pedido_service.buscar_pedido_por_id")
def test_atualizar_pedido_lanca_404_quando_restaurante_nao_existe(
    mock_buscar_pedido,
    mock_buscar_restaurante
):
    banco_mock = MagicMock()

    pedido_mock = MagicMock()

    mock_buscar_pedido.return_value = pedido_mock
    mock_buscar_restaurante.return_value = None

    dados = PedidoAlteracao(
        restaurante_id=999
    )

    with pytest.raises(HTTPException) as erro:
        atualizar_pedido(
            banco_mock,
            1,
            dados
        )

    assert erro.value.status_code == 404
    assert erro.value.detail == "Restaurante não encontrado"


@patch("app.services.pedido_service.buscar_pedido_por_id")
@patch("app.services.pedido_service.deletar")
def test_deletar_pedido_chama_dao_quando_pedido_existe(
    mock_deletar,
    mock_buscar_pedido
):
    banco_mock = MagicMock()

    pedido_mock = MagicMock()

    mock_buscar_pedido.return_value = pedido_mock

    resultado = deletar_pedido(
        banco_mock,
        1
    )

    mock_deletar.assert_called_once_with(
        banco_mock,
        pedido_mock
    )

    assert resultado == pedido_mock


@patch("app.services.pedido_service.buscar_pedido_por_id")
@patch("app.services.pedido_service.deletar")
def test_deletar_pedido_nao_chama_dao_quando_pedido_nao_existe(
    mock_deletar,
    mock_buscar_pedido
):
    banco_mock = MagicMock()

    mock_buscar_pedido.return_value = None

    resultado = deletar_pedido(
        banco_mock,
        1
    )

    mock_deletar.assert_not_called()

    assert resultado is None
