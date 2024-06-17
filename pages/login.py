import dash
from dash import html, dcc
from utils.helpers import iconify
import dash_mantine_components as dmc 

dash.register_page(__name__)
from dash_iconify import DashIconify


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

loginWithGoogleStyle =   {
    "textDecoration": "white",
    "borderRadius": "50px",
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
                    dmc.Text("Sign in ",  size='xl', fw=700),
                    dmc.Text("Please log in to continue", c='gray', size='xs', mb = 10),
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
                        children="Sign in", 
                        n_clicks=0, 
                        type="submit", 
                        id="login-button", 
                        style =loginButtonStyle
                    ),
                    dmc.Divider(label="Or continue with", mb = 10, mt = 10),
                    html.A(
                        href='/signingoogle', 
                        style = loginWithGoogleStyle,
                        children = [
                            dmc.Button(
                                "Google",
                                variant="outline",
                                color = "#E418C2ff",
                                fullWidth=True,
                                radius='xl',
                                leftSection=DashIconify(icon="flat-color-icons:google"),
                            ),
                        ]
                    ),
                    dmc.Flex(
                         mt = 10,
                        align = 'center',
                        children = [
                            dmc.Text(f" Don't have and Account?", c='gray', size = 'xs'),
                            html.A('Sign up', href='/register', style = {'fontSize':'12px'})
                        ]
                    )  
                ]
            )
        ]
    )
)


