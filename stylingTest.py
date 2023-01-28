import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html

app = dash.Dash(
    __name__,
    external_scripts="https://cdn.tailwindcss.com"
)

app.scripts.config.serve_locally = True

app.layout = html.Div(
    children=[
        html.H1(children="Dash With Tailwind",
        className="text-sky-400")
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)