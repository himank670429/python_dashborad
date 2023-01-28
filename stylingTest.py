import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html

external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]

app = dash.Dash(
    __name__,
    external_scripts=external_script
)
app.scripts.config.serve_locally = True

app.layout = html.Div(
    children="Auction Of Bytes",
    className="w-full h-screen bg-sky-200 font-sans text-8xl flex justify-center align-center text-cyan-400"
)


if __name__ == "__main__":
    app.run_server(debug=True)