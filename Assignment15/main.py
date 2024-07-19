from fastapi import FastAPI
from sqlmodel import Field, SQLModel, create_engine, Session, select
import sqlite3
import psycopg2

app = FastAPI()

@app.get("/")
def registered_users():
    # DATABASE_URL = "postgresql://parisa:110@some-postgres:5432/postgres"
    # engine = create_engine(DATABASE_URL, echo=True)
    # SQLModel.metadata.create_all(engine)
    # connection = psycopg2.connect(database="database", user="parisa", password="110", host="localhost", port=5432)
    # cursor = connection.cursor()
    # users = cursor.execute("SELECT * from portal.portal_users;")
    # # Fetch all rows from database
    # record = cursor.fetchall()
    # return {"Count of registedred users" : len(users.fetchall())} 

    # with Session(engine) as db_session:
    #         statement = select(User)

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    users = cursor.execute("SELECT * FROM user")

    return {"Count of registedred users" : len(users.fetchall())} 



