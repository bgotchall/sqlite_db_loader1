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
#app = dash.Dash(__name__)
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
###############################################################################
# example sankey:

# fig = go.Figure(data=[go.Sankey(
#     node = dict(
#       pad = 15,
#       thickness = 20,
#       line = dict(color = "black", width = 0.5),
#       label = ["W1", "W2", "probe fail", "probe pass", "assy fail", "assy pass"],
#       color = ["blue", "red"]
#     ),
#     link = dict(
#       source = [0, 0,   1,    1   ,3     ,3], # indices correspond to labels, eg A1, A2, A1, B1, ...
#       target = [2, 3,   2,    3   ,4     ,5],
#       value = [50, 450, 40, 460   ,20    ,890 ]
#   ))])

# fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
# fig.show()

import json
import urllib

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
response = urllib.request.urlopen(url)
data = json.loads(response.read())

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="graph"),
    html.P("Opacity"),
    dcc.Slider(id='opacity', min=0, max=1, 
               value=0.5, step=0.1)
])

@app.callback(
    Output("graph", "figure"), 
    [Input("opacity", "value")])
def display_sankey(opacity):
    opacity = str(opacity)

    # override gray link colors with 'source' colors
    node = data['data'][0]['node']
    link = data['data'][0]['link']

    # Change opacity
    node['color'] = [
        'rgba(255,0,255,{})'.format(opacity) 
        if c == "magenta" else c.replace('0.8', opacity) 
        for c in node['color']]

    link['color'] = [
        node['color'][src] for src in link['source']]

    fig = go.Figure(go.Sankey(link=link, node=node))
    fig.update_layout(font_size=10)

    return fig

app.run_server(debug=True)








#print(df.head())
#cur=con.cursor()

#print(lot_names)

con.close()

