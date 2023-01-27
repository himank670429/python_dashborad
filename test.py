from dash import Dash, html, Input, Output, callback
updated : int = 0
@callback(
    Output(component_id="status", component_property="children"),
    [Input(component_id="status", component_property="children")]
)
def a(b):
    pass
app = Dash(__name__)
app.layout = html.Div({
    html.Label(id = "status", children="Loading")
})
app.run()