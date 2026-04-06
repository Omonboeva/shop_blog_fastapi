from fastapi import FastAPI
from app.database import engine, Base
from app import models

# Jadvallarni avtomatik yaratadi
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Shop API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Shop API ishlamoqda!"}