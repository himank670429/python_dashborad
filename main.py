from dash import Dash, html, Input, Output, callback
import pandas as pd

url = r"https://docs.google.com/spreadsheets/d/e/2PACX-1vSzEDkDrgBh65x57aSFARUK_5jxlciUa_C8hZK5cDWeAe8Oo4j4ysypG0Ajl4RADpY7ZPdkwT14Y8dO/pub?gid=0&single=true&output=csv"

@callback(
    Output(component_id='container',component_property='children'),
    Input(component_id='btn', component_property='n_clicks'),
)



def generate_tables(n_clicks):
    # data_frame = pd.read_excel("data.xlsx")
    data_frame = pd.read_csv("data.csv")
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
        html.H1(children = "Auction Of Bytes"),
        html.Div(id = "container", children = ""),
        html.Button(id = 'btn',children = 'Refresh Data', n_clicks = 0)
    ]
)

if __name__ == "__main__":
    app.run(debug = True)