from unittest.mock import patch
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

@patch(
    "app.routes.pedido_routes.criar_pedido"
)
@patch(
    "app.routes.pedido_routes.buscar_restaurante_por_id"
)
def test_criar_pedido(
    mock_buscar_restaurante,
    mock_criar_pedido
):
    mock_buscar_restaurante.return_value = {
        "id": 1,
        "nome": "Pizza Max"
    }

    mock_criar_pedido.return_value = {
        "id": 1,
        "prato_principal": "Hamburguer",
        "acompanhamento": "Batata",
        "observacao": "Sem cebola",
        "valor": 30.0,
        "restaurante_id": 1,
        "created_at": "2026-01-01T10:00:00",
        "updated_at": "2026-01-01T10:00:00"
    }

    response = client.post(
        "/pedidos/",
        json={
            "prato_principal": "Hamburguer",
            "acompanhamento": "Batata",
            "observacao": "Sem cebola",
            "valor": 30.0,
            "restaurante_id": 1
        }
    )

    assert response.status_code == 200
    dados = response.json()
    assert dados["prato_principal"] == "Hamburguer"
