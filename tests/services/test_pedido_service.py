from unittest.mock import patch, MagicMock

from app.services.pedido_service import (
    criar_pedido,
    buscar_pedido_por_id
)
from app.schemas.pedido_schema import (
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
