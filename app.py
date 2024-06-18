


from dash import (
    Dash, html, ALL, dcc, callback, Input, Output, State, 
    clientside_callback, ClientsideFunction,
    _dash_renderer, page_registry, page_container, no_update, set_props
)
from flask import Flask, request, redirect, session, url_for
import json, os
import dash_mantine_components as dmc

from authlib.integrations.flask_client import OAuth

# Internal Imports
from components.header import header
from components.sidebar import sidebar
from utils.helpers import iconify
from appconfig import stylesheets

_dash_renderer._set_react_version("18.2.0")

with open('db.json', 'r') as openfile:
    db = json.load(openfile)
 

server = Flask(__name__)
server.config.update(SECRET_KEY=os.getenv("SECRET_KEY"))

app = Dash(
    __name__, server=server, use_pages=True,
    external_stylesheets=stylesheets,
)

server = app.server

oauth = OAuth(server)

google = oauth.register(
    name='google',
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    api_base_url='https://www.googleapis.com/oauth2/v3/',
    client_kwargs={'scope': 'openid profile email'}
)

app.layout = dmc.MantineProvider(
    id="mantine-provider",
    children = [
        dmc.AppShell(
            id="app-shell",
            navbar={ "breakpoint": "md", "collapsed": {"mobile": True}},
            children = [
                dcc.Location(id="url"),
                dmc.AppShellHeader(header()),
                dmc.AppShellNavbar(sidebar, withBorder=True),
                dmc.AppShellMain(page_container),
            ]
        )
    ]   
)

@server.route('/login', methods=['POST'])
def login_button_click():
    if request.form:
        email = request.form['email']
        password = request.form['password']
        user = db.get(email)
        if user and user['password'] == password:
            session['email'] = user
            return redirect('/secret')
        else:
            return """invalid username and/or password <a href='/login'>login here</a> or register here <a href='/register'>register here</a> """

@server.route('/register', methods=['POST'])
def register_button_click():
    if request.form:
        given_name = request.form['given_name']
        family_name = request.form['family_name']
        email = request.form['email']
        password = request.form['password']
        user = db.get(email, None)
        if user :
            return f""" user name {user } is taken chose another one and continue <a href='/register'>register here</a> """
        else:
            db[email]= {"given_name": given_name,  "family_name":family_name, "email": email, "password":password}
            with open("db.json", "w") as outfile: 
                json.dump(db, outfile, indent=4)
            return redirect('/login')
        
# Flask routes for OAuth
@server.route('/signingoogle')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@server.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    resp.raise_for_status()
    user_info = resp.json()
    session['email'] = user_info
    return redirect('/')

@callback(
    Output('avatar-indicator', 'children'),
    Input("url", "pathname"),
)
def update_user_initials(url):
    user =''
    image=''
    size=0
    if  url =='/logout':
        user = ""
        size=0
    elif 'email' in session:
        acount = session['email']
        user = f"{acount.get('given_name', '')[:1]}{acount.get('family_name', '')[:1]}"
        image = acount.get('picture', '')
     
        size=8
    status = dmc.Indicator(
            dmc.Avatar(
                style = {"cursor": "pointer" },
                size="md",
                radius="xl",
                src=image,
            ),
            offset=3,
            position="bottom-end",
            styles={
                "indicator": {"height": '20px', "padding": '2px', 'paddingInline':'0px'},
            },
            color='dark',
            size=size,
            label = user,
            withBorder=True,
            id = 'indicator'
        )
    return  status

clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='theme_switcher_callback'
    ),
    Output("mantine-provider", "theme"),
    Output("mantine-provider", "forceColorScheme"),
    Output("color-scheme-toggle", "rightSection"),
    Output("color-scheme-toggle", "label"),
    Input("color-scheme-toggle", "n_clicks")

)
clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='side_bar_toggle'
    ),
    Output("app-shell", "navbar"),
    Input("burger-button", "opened"),
    State("app-shell", "navbar"),

)

if __name__ == "__main__":
    app.run_server(debug=True, port= 8050)

