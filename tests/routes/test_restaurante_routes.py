from unittest.mock import patch
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

@patch(
    "app.routes.restaurante_routes.criar_restaurante"
)
def test_criar_restaurante(
    mock_criar_restaurante
):
    mock_criar_restaurante.return_value = {
        "id": 1,
        "nome": "Pizza Max",
        "rua": "Rua A",
        "bairro": "Centro",
        "numero": 10,
        "cidade": "Fortaleza",
        "categoria": "Pizza",
        "created_at": "2026-01-01T10:00:00",
        "updated_at": "2026-01-01T10:00:00"
    }

    response = client.post(
        "/restaurantes/",
        json={
            "nome": "Pizza Max",
            "rua": "Rua A",
            "bairro": "Centro",
            "numero": 10,
            "cidade": "Fortaleza",
            "categoria": "Pizza"
        }
    )

    assert response.status_code == 200
    dados = response.json()
    assert dados["nome"] == "Pizza Max"
