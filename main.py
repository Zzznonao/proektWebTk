from fastapi import FastAPI
from salimov import funkSalimov

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello"}

@app.get("/funcFIO")
def get_funkSalimov(x: int, y: int):
    return {"result": funkSalimov(x, y)}