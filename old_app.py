import dash
from dash import html
from dash import dcc
from dash.exceptions import PreventUpdate
from dash import Output, Input
from datetime import datetime
import json

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
    
    html.Div(id = 'output', children = [], style = {"font-size" : 16}),

])

@app.callback(
    [Output('output', 'children')],
    [Input('my_interval', 'n_intervals')]
)
def dataFeed(num):
    if num == 0:
        raise PreventUpdate
    else:
        time = datetime.now()
        data = {"time" : time}
        data = json.dumps(data, default=str)
        return [data]

if __name__ == '__main__':
    app.run_server()
