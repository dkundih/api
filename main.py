from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware 
from datetime import datetime
import time
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

class Middleware(BaseHTTPMiddleware):
    async def dispatch(self, request :Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["Time"] = str(process_time)
        return response
    

origins = ["https://dkundih-api.herokuapp.com",
           "http://127.0.0.1:8080",
           "http://127.0.0.1:8000",
           "https://promet-kc.netlify.app",
           ]

app.add_middleware(Middleware)
app.add_middleware(CORSMiddleware, allow_origins = origins)

@app.get("/")
async def hi():
    rn = datetime.now().replace(microsecond=0)
    now = rn.time()
    output = {"Pozdrav" : "Od Davida",
              "Vrijeme" : now}
    return output
