from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware 
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
    

origins = ["https://dkundih-api.herokuapp.com", "https://promet-kc.netlify.app", "https://localhost:3000", "https://localhost:8000", "https://localhost:5000", "https://localhost:8080"]

app.add_middleware(Middleware)
app.add_middleware(CORSMiddleware, allow_origins = origins)

@app.get("/")
async def hi():
    return {"Hello" : "World"}
