import sqlite3
import dash
import dash_table
import plotly
import plotly.graph_objects as go
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


con = sqlite3.connect(".\data\qep_production.db")
df=pd.read_sql_query('SELECT * FROM LotInsertionTableModel',con)


app = dash.Dash(__name__)
server = app.server

lot_names=df.Lotid.unique()
app = dash.Dash(__name__)
#here I can start dumping in example displays with this simple data table


###############################################################################
#this works to just show a table.  Note this script runs a server at 127.0.0.1:8050


app.layout = html.Div([
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} 
                 for i in df.columns],
        data=df.to_dict('records'),
        style_cell=dict(textAlign='left'),
        style_header=dict(backgroundColor="paleturquoise"),
        style_data=dict(backgroundColor="lavender")
    )
])
###############################################################################
# try a bar chart of say yields:




app.run_server(debug=True)






#print(df.head())
#cur=con.cursor()

#print(lot_names)

con.close()

