from threading import Timer
from datetime import datetime
import requests

def dataFeed():
    data = {"Time" : datetime.now()}
    r = requests.post("https://httpbin.org/post", params = data)
    f = r.text
    Timer(5.0, dataFeed).start()
    print(f)
    return f

dataFeed()
