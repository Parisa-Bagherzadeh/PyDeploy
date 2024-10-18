from pymongo import MongoClient
from fastapi import FastAPI
from .tasks import add_number

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello world!"}

client = MongoClient("mongodb://mongodb:27017/")    
db = client.ekyc_db

@app.get("/add_sampe/")
def add_sample():
    db.users.insert_one({"name":"Parisa"})
    return {"message": "User added"}

@app.get("/add/")
def add_numbers_route(a: int,b: int):
    task = add_numbers.delay(a, b)
    return {"task_id": task.id}
