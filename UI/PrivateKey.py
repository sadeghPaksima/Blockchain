from dash import dcc
import dash_bootstrap_components as dbc
def create_private_item():
    return dbc.Col(
        dcc.Textarea(
            id='Private-key',
            style={'width': '100%', 'height': 300},)
    )