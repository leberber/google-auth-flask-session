
from dash import (
    html, dcc, Output, Input, callback, 
    register_page
)
from flask import session
import json
import dash_mantine_components as dmc
from flask_login import current_user

register_page(__name__)



def layout(**kwargs):
    if 'email' in session:
        acount = session['email']
        acount = json.dumps(acount, indent=4)
        return dmc.Center(
                    mt= 50, pt=50,
                    children = [   
                        dmc.Paper(
                        pt=20,
                        shadow='sm',
                        children=[
                            dmc.Text("Here are your account details"),
                            dmc.CodeHighlight(
                                language="json",
                                code=str(acount),
                            )
                        ]
                    )
                ]
            )


      

    else:   
        return dmc.Center(
            m = 30,
            children =[
                dmc.Flex(
                    align="center",
                    children=[
                        dmc.Text("This page requires login. Please", p =5),
                        html.A('login', href='/login'),
                        dmc.Text("to continue", p = 5),
                    ]
                )
            ]
        )



