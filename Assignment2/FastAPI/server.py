from fastapi import FastAPI

app = FastAPI()

@app.get("/Parisa")
def read_root():
    return {"Hello":"World"}