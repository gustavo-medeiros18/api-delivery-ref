from fastapi import FastAPI

from app.banco_de_dados import (
    Base,
    engine
)
from app.routes.restaurante_routes import router_restaurantes
from app.routes.pedido_routes import router_pedidos

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Delivery"
)

app.include_router(router_restaurantes)
app.include_router(router_pedidos)

@app.get("/")
def inicio():
    return {
        "mensagem": "API Delivery funcionando"
    }