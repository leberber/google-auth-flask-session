import dash
from dash import html, dcc
from utils.helpers import iconify
import dash_mantine_components as dmc 



dash.register_page(__name__)

loginButtonStyle =   {
    "background": "#E418C2ff",
    "padding": "5px 20px" ,
    "border": "none",
    "borderRadius": "20px",
    "color": "white",
    "fontSize":"16px",
    "width":"100%"
    
  }

layout = dmc.Center(
    dmc.Paper(
        shadow='sm',
        p = "30px",
        mt = 60,
        children = [
            html.Form(
                style = {"width":'300px'},
                method='POST',
                children = [
                    dmc.Text("Sign up",  size='xl', fw=700),
                    dmc.Text("Please up in to continue", c='gray', size='xs', mb = 10),
                    dmc.TextInput(
                        label="First Name",
                        name='given_name',
                        placeholder="Enter your first name",
                        required = True,
                    ),
                    dmc.TextInput(
                        label="Last Name",
                        name='family_name',
                        placeholder="Enter your last name",
                        required = True,
                    ),
                    dmc.TextInput(
                        label="Email",
                        name='email',
                        placeholder="Enter your Email",
                        required = True,
                        leftSection=iconify(icon="ic:round-alternate-email", width=20),
                    ),
                    dmc.PasswordInput(
                        mb=20,
                        label="Password",
                        placeholder="Enter your password",
                        leftSection=iconify(icon="bi:shield-lock", width=20),
                        name='password',
                        required = True
                    ),
                    html.Button(
                        children="Sign up", 
                        n_clicks=0, 
                        type="submit", 
                        id="register-button", 
                        style =loginButtonStyle
                    ),
                    dmc.Flex(
                         mt = 10,
                        align = 'center',
                        children = [
                            dmc.Text(f"Already have an Account?", c='gray', size = 'xs'),
                            html.A('Sign in', href='/login', style = {'fontSize':'12px'})
                        ]
                    )  
                ]
            )
        ]
    )
)