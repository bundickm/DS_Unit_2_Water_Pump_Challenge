import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app


column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process

            To see how the model was developed and refined you can [go here](https://github.com/bundickm/Predictive_Preventative_Maintenance/blob/master/Tanzania%20Water%20Pump%20Challenge.ipynb) 
            and read my notebook that walks through the whole process.

            To see how this application was made, visit [here]() 
            to peak under the hood at the code.
            """
        ),

    ],
)

layout = dbc.Row([column1])