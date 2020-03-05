# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import numpy as np

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ### Predict Pump Status

            """
        ),
        dcc.Markdown("""##### Quantity"""),
        html.Div([dcc.Dropdown(
            id='quantity',
            options=[
                {'label': 'Insufficient', 'value': 1},
                {'label': 'Enough', 'value': 2},
                {'label': 'Seasonal', 'value': 3},
                {'label': 'Dry', 'value': 4},
                {'label': 'Unknown', 'value': 5},
            ],
        value=1,
        )], style={'marginBottom': '10px'}),

        dcc.Markdown("""##### Extraction Type"""),
        html.Div([dcc.Dropdown(
            id='extraction_type',
            options=[
                {'label': 'Gravity', 'value': 1},
                {'label': 'Hand Pump', 'value': 2},
                {'label': 'Other', 'value': 3},
                {'label': 'Motor Pump', 'value': 4},
                {'label': 'Submersible', 'value': 5},
                {'label': 'Wind Powered', 'value': 6},
                {'label': 'Rope Pump', 'value': 7},
            ],
        value=1,
        )], style={'marginBottom': '10px'}),

        dcc.Markdown("""##### Waterpoint Type"""),
        html.Div([dcc.Dropdown(
            id='waterpoint_type',
            options=[
                {'label': 'Communal Standpipe', 'value': 1},
                {'label': 'Hand Pump', 'value': 2},
                {'label': 'Other', 'value': 3},
                {'label': 'Communal Standpipe Multiple', 'value': 4},
                {'label': 'Improved Spring', 'value': 5},
                {'label': 'Cattle Trough', 'value': 6},
                {'label': 'Dam', 'value': 7},
            ],
        value=1,
        )], style={'marginBottom': '10px'}),

        dcc.Markdown("""##### Population"""),
        html.Div([dcc.Input(
            id='population',
            type='number',
            placeholder="Max Pop. 30500",
            value=0,
            min=0,
            max=30500)
        ], style={'marginBottom': '10px'}),

        dcc.Markdown("""##### Total Static Head"""),
        html.Div([dcc.Input(
            id='tsh',
            type='number',
            placeholder="Max TSH 1500",
            value=0,
            min=0,
            max=1500),
        ], style={'marginBottom': '10px'}),

        dcc.Markdown("""##### Coordinates"""),
        dbc.Row([
            dcc.Input(id='lat',
                      type='number',
                      placeholder="Lat.  -11.6 to -.999",
                      value=-11.649440,
                      min=-11.649440,
                      max=-0.998464),
            dcc.Input(id='lon',
                      type='number',
                      placeholder="Long.  25.2 to 40.3",
                      value=25.171774,
                      min=25.171774,
                      max=40.345193),
        ], className='coord'),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('''## Results'''),
        html.Div(id='prediction-content',
                 className='lead',
                 style={'marginBottom': '10px'}),
        dcc.Markdown('''
        ### Information

        The results here are based off a simplified model that uses 
        just these 7 variables. This simplification results in a 2% 
        decrease in overall accuracy to 79%, but this tradeoff allows for 
        greater interpretability. A user in the field can focus on 
        just 7 data points instead of the 17 in the full model and 
        still have a high level of certainty in the prediction.

        - **Quantity**: Amount of water the well produces
        - **Extraction Type**: The kind of extraction the waterpoint uses
        - **Waterpoint Type**: The kind of waterpoint
        - **Population**: Size of the population using the well, 0 to 30500
        - **Total Static Head**: The amount of water available to 
        the waterpoint, 0 to 1500
        - **Latitude**: GPS Coordinate, -11.649440 to -0.998464
        - **Longitude**: GPS Coordinate, 25.171774 to 40.345193
        ''')
    ]
)

@app.callback([Output('prediction-content', 'children')],
              [Input('quantity', 'value'), Input('extraction_type', 'value'), 
               Input('waterpoint_type', 'value'), Input('population', 'value'), 
               Input('tsh', 'value'), Input('lat', 'value'), Input('lon', 'value')],)
def predict(quantity, extraction_type, waterpoint_type,
            population, tsh, lat, lon):
    model = load('assets/model.joblib')
    input_values = np.array([quantity, extraction_type, waterpoint_type,
                             tsh, population, lat, lon]).reshape(1, -1)
    prediction = model.predict(input_values)
    pred_proba = max(model.predict_proba(input_values)[0])*100
    return [f'Based on the input you provided, your waterpump is likely to be: {prediction[0]}. '
            f'The model is {pred_proba:.2f}% certain of the predicted status.']

layout = dbc.Row([column1, column2])