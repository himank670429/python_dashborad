from dash import Dash, html
import pandas as pd

# just a comment
# generating table for dash board
def generate_tables(data_frame : pd.DataFrame):
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

# import data
df = pd.read_excel("data.xlsx")

# app layout
app.layout = html.Div(
    children = [
        html.H1(children = "Aution Of Bytes"),
        generate_tables(df)
    ]
)

if __name__ == "__main__":
    app.run_server(debug = True)