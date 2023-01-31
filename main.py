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
    # data_frame = get_data(url , sheet_name)
    data_frame = pd.read_csv("data.csv")
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in data_frame.columns] , 
            className='''text-[#FFFFFF]
                        text-2xl border-[3px] bg-[#1B6C80] border-[#03FFFF]''')
        ),
        html.Tbody([
            html.Tr([
                html.Td(data_frame.iloc[row][col] , className='''border-2''') for col in data_frame.columns
            ])
            for row in range(len(data_frame))
        ], className='''text-center
                        text-lg text-[#FFFFFF] border-2 ''')
    ] , className="reaponsive-table w-full border-[#03FFFF] table-fixed", )


# creating app
app = Dash(
    __name__,
    external_scripts=external_script
)
app.scripts.config.serve_locally = True
app.layout = html.Div([
    # Title banner
    html.Div([
        html.Img(src="./static/assets/tm-logo.png", width="70px" , height="auto") , 
        html.H1(children="Auction of Bytes" , 
                className='''ml-[15px] text-6xl font-bold text-[#FFEFF2]''')
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
        
        className='''mx-4 shadow-2xl shadow-[#3FFFFF]/50'''
    ),

    
    # Footer
    html.Div([
        html.Div(
        # Tech marathon
        children = (html.A(href="http://techmarathon.in/", children=[
            html.Img(src = "./static/assets/tm-logo.png", width='50px', height='auto'),
            ],className="flex"),
            )
        ),
        html.Div(
            children=(
                html.H5(children = "In Collaboration With", 
                className = '''mt-[10px] text-[#FFFFFF] mx-[20px]''')
            )
        )
        ,
        html.Div(
        # Sanganika
        children = (html.A(href="https://www.instagram.com/sanganika_dduc/" , children=[
            html.Img(src="./static/assets/sanganika-logo.png", width='50px', height='auto'),
            ], className="flex")
            )
        )
    ] , 
    className='''flex align-center justify-center mt-[10px]'''),
],
className='''bg-gradient-to-br from-[#40C0CB] to-[#002133] via[#04165D] w-full h-screen''')
#bg-gradient-to-br from-[#04165D] to-[#40C0CB]
html.style= '''@import url('https://fonts.googleapis.com/css2?family=Quicksand&display=swap');
               font-family : "Quicksand" , sans-serif; '''

if __name__ == "__main__":
    app.run(debug = True)