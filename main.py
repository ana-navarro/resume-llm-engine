from fastapi import FastAPI

from applications.routes.prompt_routes import router as prompt_router

app = FastAPI()


@app.get("/")
def ler_raiz():
  return {"mensagem": "Olá, Mundo!"}


app.include_router(prompt_router)
