from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    time = datetime.now()
    return time
