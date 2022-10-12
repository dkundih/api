from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware 
from datetime import datetime
import time
import pytz
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
async def osnovno():
    datum = datetime.now().replace(microsecond=0).astimezone(pytz.timezone('Europe/Zagreb'))
    vrijeme = datum.time()
    output = {"Pristup omogućuje" : "David Kundih",
              "Izvorni kod" : "https://github.com/dkundih/api",
              "Poslužuje" : "https://promet-kc.netlify.app // https://github.com/dkundih/promet-kc",
              "Licenca" : "Apache 2.0",
              "Vrijeme" : vrijeme,
              }
    return output

@app.get("/meta")
async def meta():
    output = {"Upozorenje" : "Stvarno ne bi trebao biti na ovoj adresi (:",}
    return output
