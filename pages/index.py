import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predicting the Functional Status of Waterpumps

            This problem can be viewed as a proof of concept for the power 
            of predictive modeling for preventative maintenance. Preventative 
            maintenance is generally cheaper than replacement or repair of a 
            broken item. In addition, you can schedule the maintenance to 
            minimize downtime or impact on the business or service. 
            
            Why predictive instead of just regularly scheduled preventative 
            maintenance though? Because again we see savings. By only 
            allocating resources when needed we reduce maintenance or labor 
            for inspections on fully functional machines but also identify 
            problems inside the inspection intervals.

            """
        ),
        dcc.Link(dbc.Button('Make a Prediction', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/waterpump.jpg',
                 className='img-fluid float-right',
                 alt='Waterpump Image')
    ]
)

layout = dbc.Row([column1, column2])