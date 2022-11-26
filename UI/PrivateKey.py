from dash import dcc
import dash_bootstrap_components as dbc
def create_private_item(value):
    return dbc.Col(
        dcc.Textarea(
            id='Private-key',value=value,
            style={'width': '100%', 'height': 300},)
    )