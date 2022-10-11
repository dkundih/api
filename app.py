import dash
from dash import html
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

#APP
app = dash.Dash(__name__)
server = app.server
app.title = 'dkundih-promet'


app.layout = html.Div([
    
    html.Div([
    html.A("{APP RUNNING}"),
    ], id = 'body'),

])

if __name__ == '__main__':
    app.run_server()
