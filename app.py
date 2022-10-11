from re import I
import dash
from dash import html
from dash import dcc
from dash.exceptions import PreventUpdate
from dash import Output, Input
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
        dcc.Interval(
            id = 'my_interval',
            disabled = False,
            interval = 1 * 5000,
            n_intervals = 0,
        )
    ]),
    
    html.Div(id = 'output', children = [], style = {"font-size" : 36}),

])

@app.callback(
    [Output('output', 'children')],
    [Input('my_interval', 'n_intervals')]
)
def dataFeed(num):
    if num == 0:
        raise PreventUpdate
    else:
        data = {"Time" : datetime.now()}
        r = requests.post("https://httpbin.org/post", params = data)
        output = r.text
        return [output]

if __name__ == '__main__':
    app.run_server()
