import dash_bootstrap_components as dbc
import dash_daq as daq
from dash import html,Input,Output,State,dcc,Dash
from UI import menu,Style,KeysUI
from CryptographyBlockchain import CreateKeys 
from urllib.parse import unquote

app=Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout=html.Div([dcc.Location(id="url"),dbc.Row([dbc.Col(menu.Create_Card())],id="Main"),dbc.Row(children=[],id="item")],id="root",className="container-fluid",style=Style.MarginTop)

@app.callback(
    Output(component_id="Main",component_property= 'style'),
    Output(component_id="item",component_property= 'children'),
    Input(component_id="url",component_property="pathname"),
)
def render(pathname):
    if pathname=='/':
        return Style.DisplayBlock,[]
    else:
        url=unquote(pathname)[1:]
        if url in menu.menu_list:
            functions={"Create Private key":KeysUI.create_Keys_UI}
            private_key,public_key=CreateKeys.Create_keys()
            d=functions[url](private_key,public_key)
            return Style.DisplayNone,d
        

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=True,port=9999)