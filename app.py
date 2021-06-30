# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#DFDAE3',
    'text': '#111111'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('df.csv')
df = df.head(20)
df = df.rename(columns={'token0symbol':'Times Traded','Unnamed: 0':'Token Symbol'})
df.index.names = ['0'] 

fig = px.bar(df, x="Token Symbol", y="Times Traded", color="Token Symbol", barmode="relative" )


fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Token Analytics',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Number of times a token has been traded in a pair.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig,
        style={'width': '90vh', 'height': '90vh'}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)