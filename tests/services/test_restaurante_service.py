from unittest.mock import patch, MagicMock

from app.services.restaurante_service import (
    criar_restaurante,
    buscar_restaurante_por_id,
    atualizar_restaurante,
    deletar_restaurante
)

from app.schemas.restaurante_schema import (
    RestauranteCriacao,
    RestauranteAlteracao
)

@patch("app.services.restaurante_service.criar")
def test_criar_restaurante(
    mock_criar
):
    banco_mock = MagicMock()

    restaurante_schema = RestauranteCriacao(
        nome="Pizza Max",
        rua="Rua A",
        bairro="Centro",
        numero=100,
        cidade="Fortaleza",
        categoria="Pizza"
    )

    mock_criar.return_value = {
        "id": 1,
        "nome": "Pizza Max"
    }

    resultado = criar_restaurante(
        banco_mock,
        restaurante_schema
    )

    mock_criar.assert_called_once()

    assert resultado["nome"] == "Pizza Max"

@patch("app.services.restaurante_service.buscar_por_id")
def test_buscar_restaurante_por_id(
    mock_buscar
):
    banco_mock = MagicMock()

    mock_buscar.return_value = {
        "id": 1,
        "nome": "Pizza Max"
    }

    resultado = buscar_restaurante_por_id(
        banco_mock,
        1
    )

    mock_buscar.assert_called_once_with(
        banco_mock,
        1
    )

    assert resultado["id"] == 1

@patch("app.services.restaurante_service.buscar_restaurante_por_id")
@patch("app.services.restaurante_service.atualizar")
def test_atualizar_restaurante(
    mock_atualizar,
    mock_buscar
):
    banco_mock = MagicMock()
    restaurante_existente = MagicMock()

    mock_buscar.return_value = restaurante_existente
    mock_atualizar.return_value = {
        "id": 1,
        "nome": "Novo Nome"
    }

    dados = RestauranteAlteracao(
        nome="Novo Nome"
    )

    resultado = atualizar_restaurante(
        banco_mock,
        1,
        dados
    )

    assert resultado["nome"] == "Novo Nome"


@patch("app.services.restaurante_service.buscar_restaurante_por_id")
@patch("app.services.restaurante_service.deletar")
def test_deletar_restaurante(
    mock_deletar,
    mock_buscar
):
    banco_mock = MagicMock()
    restaurante_mock = MagicMock()
    
    restaurante_mock.pedidos = []
    mock_buscar.return_value = restaurante_mock
    resultado = deletar_restaurante(
        banco_mock,
        1
    )
    mock_deletar.assert_called_once()

    assert resultado == restaurante_mock
