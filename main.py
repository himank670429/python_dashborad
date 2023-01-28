from dash import Dash, html, Input, Output, callback, dcc
import pandas as pd
from data import get_data

external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]
url = "https://docs.google.com/spreadsheets/d/1hL94OaViPEwfEcsm238wYnjA8L5bIkHvUdxfTcYYDBQ/edit#gid=0" # enter your google sheet url here
sheet_name = "Data" # enter your google sheet name here
reload_duration = 5 # duration of page refreshing 

@callback(
    Output(component_id='container',component_property='children'),
    Input(component_id='live-update', component_property='n_intervals'),
)

def generate_tables(n_intervals):
    data_frame = get_data(url , sheet_name)
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in data_frame.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(data_frame.iloc[row][col]) for col in data_frame.columns
            ])
            for row in range(len(data_frame))
        ])
    ])


# creating app
app = Dash(__name__)

# app layout
app.layout = html.Div(
    children = [
        dcc.Interval(
            id = 'live-update',
            n_intervals = 0,
            interval = reload_duration*1000
        ),
        html.H1(children = "Auction Of Bytes"),
        html.Div(id = "container", children = "" , className="w-full h-full flex"),
    ]
)

if __name__ == "__main__":
    app.run(debug = True)