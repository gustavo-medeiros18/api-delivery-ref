from fastapi import FastAPI

from app.banco_de_dados import (
    Base,
    engine
)
from app.routes.restaurante_routes import (
    router as rotas_restaurante
)
from app.routes.pedido_routes import (
    router as rotas_pedido
)

from app.models.restaurante_model import Restaurante
from app.models.pedido_model import Pedido


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Delivery"
)

app.include_router(rotas_restaurante)
app.include_router(rotas_pedido)

@app.get("/")
def inicio():
    return {
        "mensagem": "API Delivery funcionando"
    }