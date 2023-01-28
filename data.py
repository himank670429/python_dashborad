import pandas as pd
'''
This function will read the data from google sheets and store the data into a pandas DataFrame.

params - 
    url - url of the google sheets file
    sheet_name - name of the sheet
'''
def get_data(url, sheet_name):
    sheet_id = url.split('/')[-2]
    csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    # print (csv_url)
    data_frame = pd.read_csv(csv_url)
    # print (data_frame)
    return pd.read_csv(csv_url)
