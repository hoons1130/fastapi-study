from fastapi import FastAPI
from controller import items
from controller import users
from database import test_connection, Base,engine
from models.item import Item
from controller.predict import router as predict_router

app = FastAPI()
app.include_router(items.router)
app.include_router(predict_router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.on_event("startup")
def start():
    test_connection()