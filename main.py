from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API chal rahi hai 🚀"}

@app.get("/user/{id}")
def get_user(id: int):
    return {"id": id}