from dash import Dash, html, Input, Output, callback, dcc
import pandas as pd
from data import get_data

external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]
url = "https://docs.google.com/spreadsheets/d/1hL94OaViPEwfEcsm238wYnjA8L5bIkHvUdxfTcYYDBQ/edit#gid=0" # enter your google sheet url here
sheet_name = "Data" # enter your google sheet name here
reload_duration = 5 # duration of page refreshing 

FONT_COLOR = "#000000"
TABLE_BORDER = "#000000"
SHADOW_COLOR = "#000000"

@callback(
    Output(component_id='container',component_property='children'),
    Input(component_id='live-update', component_property='n_intervals'),
)

def generate_tables(n_intervals):
    # data_frame = get_data(url , sheet_name)
    data_frame = pd.read_csv("data.csv")
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in data_frame.columns] , 
            className=f'''text-[{FONT_COLOR}]
                        text-2xl border-[3px] border-[{TABLE_BORDER}]''')
        ),
        html.Tbody([
            html.Tr([
                html.Td(data_frame.iloc[row][col] , className=f'''border-2 border-x-[#BBBBBB] border-b-[#BBBBBB]''') for col in data_frame.columns
            ])
            for row in range(len(data_frame))
        ], className=f'''text-center
                        text-lg text-[{FONT_COLOR}]''')
    ] , className=f"w-full table-fixed", )


# Creating App
app = Dash(
    __name__,
    external_scripts=external_script
)
app.scripts.config.serve_locally = True
app.layout = html.Div([
    # Title banner
    html.Div([
        html.Img(src="./static/assets/tm-logo.png", width="70px" , height="auto" , className='''mr-[10px]''') , 
        html.H1(children="Auction of Bytes" , 
                className=f'''ml-[15px] text-6xl font-bold text-[#FFFFFF]'''),
        html.Img(src="./static/assets/sanganika-logo.png", width="70px" , height="auto" , className='''ml-[20px]''') , 
    ] , 
    className='''flex align-center justify-center pt-[10px]'''),
    # Main table
    html.Div(
         children = [
             dcc.Interval(
                 id = 'live-update',
                 n_intervals = 0,
                 interval = reload_duration*1000
             ),
         html.Div(id = "container", children = ""),
        ],
        
        className=f'''mx-4 mt-[20px] shadow-2xl shadow-[{SHADOW_COLOR}]/20 bg-[#FCFCFC] p-[30px] rounded-lg'''
    )
],
className=f'''bg-[url("https://img.freepik.com/free-vector/abstract-blue-tone-memphis-patterned-social-template-vector_53876-140329.jpg?w=1800&t=st=1675156875~exp=1675157475~hmac=8d82f02b0f24e6e4e402f739c1b8411c889cbf9c72c2ddd7929f441d7a4fe1b7")] bg-cover w-full h-screen''')

html.style= '''@import url('https://fonts.googleapis.com/css2?family=Quicksand&display=swap');
               font-family : "Quicksand" , sans-serif; 
                background-image : radial-gradient("#86C8BC" , "#CEEDC7");
'''

if __name__ == "__main__":
    app.run(debug = False)