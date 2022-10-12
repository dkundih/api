from fastapi import FastAPI
from datetime import datetime
import json

app = FastAPI()

@app.get("/")
def home():
    time = datetime.now()
    entry = {"Now" : time}
    return entry
