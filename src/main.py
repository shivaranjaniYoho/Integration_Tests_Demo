
from fastapi import FastAPI

from src.database import Base, engine
from src import models
from src.routes import router as customer_router
from src.webhook import router as webhook_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Integration Testing API")

app.include_router(customer_router)
app.include_router(webhook_router)

@app.get("/")
def home():
    return {"message": "Welcome to Integration Testing API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
