from threading import Timer
from datetime import datetime
import requests
import json

def dataFeed():
    r = requests.get("https://dkundih-api.herokuapp.com/")
    f = r.text
    Timer(5.0, dataFeed).start()
    print(f)
    return f

dataFeed()
