# import pandas as pd
# import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    html.H1(children='Hello, World!')
)

if __name__ == "__main__":
    app.run_server(debug=True)