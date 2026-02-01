from fastapi import FastAPI
from app.routes import router


app = FastAPI(title="QuickBite API")

app.include_router(router)


@app.get("/")
def healthcheck():
    return {"status": "API running"}
