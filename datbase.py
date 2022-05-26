import os
import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objs as go
import cdata.mysql as mod

cnxn = mod.connect("User=root;Password=;Database=test;Server=127.0.0.1;Port=3306;")

df = pd.read_sql("SELECT * FROM test", cnxn)

app_name = 'dash-mysqledataplot'
 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
 
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'CData + Dash'

trace = go.Bar(x=df.ShipName, y=df.Freight, name='ShipName')
 
app.layout = html.Div(children=[html.H1("CData Extension + Dash", style={'textAlign': 'center'}),
dcc.Graph(
id='example-graph',
figure={
'data': [trace],
'layout':
go.Layout(title='MySQL Orders Data', barmode='stack')
})
], className="container")

if __name__ == '__main__':
    app.run_server(debug=True)