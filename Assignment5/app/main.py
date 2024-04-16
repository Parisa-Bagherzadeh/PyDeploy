from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
import sqlite3
import numpy as np




task_dict = {}
app = FastAPI()


@app.get("/")
def read_root():
    return {"Welcome to my daily routine!"}

@app.get("/task")
def task():
    task_list = []
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    mytasks = cursor.execute("SELECT * FROM tasks")
    for mytask in mytasks:
        task_list.append({"id": mytask[0], "title": mytask[1], "description": mytask[2], "time": mytask[3]})
    return task_list


@app.post("/task")
def add_task(id : int = Form(), title : str = Form(), description : str = Form(), time : str = Form()):
    task_list = []
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tasks(id, title, description, time) VALUES (?, ?, ?, ?)",
                   (id, title, description, time))
    connection.commit()

    mytasks = cursor.execute("SELECT * FROM tasks")
    for mytask in mytasks:
        task_list.append({"id": mytask[0], "title": mytask[1], "description": mytask[2], "time": mytask[3]})
    return task_list

    


@app.put("/task/{id}")
def update_task(id : int, title : str = Form(None), description : str = Form(None), time : str = Form(None)):
    task_list = []
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    mytasks = cursor.execute("SELECT * FROM tasks")
    for mytask in mytasks:
        task_list.append({"id":mytask[0], "title": mytask[1], "description": mytask[2], "time": mytask[3]})


    id_exists = any(task['id'] == int(id) for task in task_list)
    
    if not id_exists : 
        raise HTTPException(status_code = 404, detail = "Task not found")
    
    if title is not None:
        for task in task_list:
            if task['id'] == int(id):
                connection = sqlite3.connect("todo.db")
                cursor = connection.cursor()
                cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (title, id))
                connection.commit()
                break

    if description is not None:
        for task in task_list:
            if task['id'] == int(id):
                connection = sqlite3.connect("todo.db")
                cursor = connection.cursor()
                cursor.execute("UPDATE tasks SET description = ? WHERE id = ?", (description, id))
                connection.commit()
                break       

        
    if time is not None:
        for task in task_list:
            if task['id'] == int(id):
                connection = sqlite3.connect("todo.db")
                cursor = connection.cursor()
                cursor.execute("UPDATE tasks SET time = ? WHERE id = ?", (time, id))
                connection.commit()
                break               

    task_list = []
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    mytasks = cursor.execute("SELECT * FROM tasks")
    for mytask in mytasks:
        task_list.append({"id":mytask[0], "title": mytask[1], "description": mytask[2], "time": mytask[3]})

    return task_list        


@app.delete("/task/{id}")
def delete_task(id : str):
    task_list = []
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    mytasks = cursor.execute("SELECT * FROM tasks")
    for mytask in mytasks:
        task_list.append({"id":mytask[0], "title": mytask[1], "description": mytask[2], "time": mytask[3]})


    id_exists = any(task['id'] == int(id) for task in task_list)
    
    if not id_exists : 
        raise HTTPException(status_code = 404, detail = "Task not found")   

    cursor.execute("DELETE FROM tasks WHERE id = ?", (id)) 
    connection.commit()