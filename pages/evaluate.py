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
        
            ## Evaluate

            Based on the exploration of the data and modeling we learn there 
            appears to be a predictive accuracy ceiling of about 82% that none 
            of the models exceed. Compared to the baseline of 54%, this is a 
            considerable gain in predictive power. We could attempt to break 
            that limit with a neural network but then we lose interpretability 
            which doesn't seem ideal when focused on repairs and 
            preventative maintenance.

            """),
        html.Img(src='assets/baseline.png',
                 className='img-fluid',
                 width='40%',
                 alt='Waterpump Image'),
        dcc.Markdown(
            """
            We also learn that the model and the accuracy is very resistant to 
            change regardless of whether engineered or direct measure. We can 
            prove this by using just the top 7 features and get above 79% 
            accuracy. This may indicate that we are missing critical 
            information that is more indicative of the status of the 
            water pump.

            Finally, depending on the stakeholder needs we have the potential 
            to tweak for precision or recall. Meaning we can play it safe and 
            have high recall so we get all broken pumps but also pull in a 
            false positives. Or, if resources are limited, we can tune for 
            precision so we know that when we spend it is not wasted.

            """
        ),

    ],
)

layout = dbc.Row([column1])