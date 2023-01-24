from dash import Dash, html, dcc, dash_table
import plotly.express as px
import pandas as pd

# creating our app
app = Dash(__name__)

# importing the data
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# creating fig
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group") # bar graph

# layout
app.layout = html.Div(
    children=[
        html.H1(children="hello Dash"),
        dcc.Graph(
            id="example-graph",
            figure=fig
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
    pass