# import requests
# timeout = 10  # Set timeout to 10 seconds


# if __name__ == '__main__':
#     response = requests.get('https://login.esso-uat.charter.com:8443/nidp/oauth/nam/.well-known/openid-configuration', timeout=timeout)
#     print(response.text)
    # app.run_server(debug=True)



from flask import Flask, url_for, redirect, session
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from authlib.integrations.flask_client import OAuth
import logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Flask server
server = Flask(__name__)
server.secret_key = 'random secret'

# Initialize OAuth
oauth = OAuth(server)

esso_uat_config = {
    "issuer": "https://login.esso-uat.charter.com:8443/nidp/oauth/nam",
    "authorization_endpoint": "https://login.esso-uat.charter.com:8443/nidp/oauth/nam/authz",
    "token_endpoint": "https://login.esso-uat.charter.com:8443/nidp/oauth/nam/token",
    "userinfo_endpoint": "https://login.esso-uat.charter.com:8443/nidp/oauth/nam/userinfo",
}

# # Register ESSO-UAT OAuth client
# # esso_uat = oauth.register(     
# #     name='esso-uat',
# #     client_id='3f6732ba-e495-4829-8717-7a30c0cbebba',
# #     client_secret='NlgqDE2-2VS3RchEjs_Sl8EA-QgdjXGiXqxy0SPcwCavgPzKFEiEeuJOfvlW3E1VxhpS4ANO7EIqCzv6er3JQg',  
# #     authorization_endpoint = 'https://login.esso-uat.charter.com:8443/nidp/oauth/nam/authz',
# #     server_metadata_url='https://login.esso-uat.charter.com:8443/nidp/oauth/nam/.well-known/openid-configuration',
# #     base_url='https://login.esso-uat.charter.com:8443/nidp/oauth/nam/',
# #     client_kwargs={'scope': 'openid profile email'}
# # )

esso_uat = oauth.register(
    name='esso-uat',
    # Client ID and Secret should be replaced with your actual values
    client_id='3f6732ba-e495-4829-8717-7a30c0cbebba',
    client_secret='NlgqDE2-2VS3RchEjs_Sl8EA-QgdjXGiXqxy0SPcwCavgPzKFEiEeuJOfvlW3E1VxhpS4ANO7EIqCzv6er3JQg',
    server_metadata_url=esso_uat_config['issuer'] + '/.well-known/openid-configuration', 
    client_kwargs={'scope': 'openid profile email'}
     # Constructing the URL based on issuer
    # Include other relevant options from the Discovery Document (optional)
    # api_base_url=esso_uat_config['...'],  # If needed for specific API calls
    # client_kwargs={'scope': '...'}  # If you need specific scopes
)

# print(help(esso_uat))
# Initialize Dash app
app = Dash(__name__, server=server, url_base_pathname='/')

# Layout of the Dash app
app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.H1("Welcome to the Dash App"),
    html.Div(id='content'),
    html.Button('Login with ESSO-UAT', id='login-button', n_clicks=0),
    html.Div(id='user-info')
])

# Flask routes for OAuth
@server.route('/login')
def login():
    esso_uat_client = oauth.create_client('esso-uat')
    # print(esso_uat_client, str(esso_uat_client))
    redirect_uri = 'https://mituat.chartercom.com/authorize'
    print("redirect_uri",redirect_uri)
    # print(esso_uat_client.authorize_redirect(redirect_uri))
    return esso_uat_client.authorize_redirect(redirect_uri)

@server.route('/authorize')
def authorize():
    esso_uat_client = oauth.create_client('esso-uat')
    # logging.debug(f'Token: {esso_uat_client}')
    
    # print('esso_uat_client', str(esso_uat_client))
    token = esso_uat_client.authorize_access_token()
    print("token", token)
    # logging.debug(f'Token: {token}')

    resp = esso_uat_client.get('userinfo')
    resp.raise_for_status()
    user_info = resp.json()
    
    session['email'] = user_info['email']
    # print(session)
    # session['samaccountname'] = user_info.get('sAMAccountName', '')
    return redirect('/')

@server.route('/')
def index():
    return "Dash app is running"

# Dash callback to update content based on URL
@app.callback(
    Output('content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if 'email' in session:
        return html.Div([
            html.H2(f"Hello, {session['email']}"),
            # html.P(f"sAMAccountName: {session['samaccountname']}"),
            html.A('Logout', href='/logout')
        ])
    else:
        return html.H2("You are not logged in.")

# Dash callback to handle login button click
@app.callback(
    Output('url', 'pathname'),
    [Input('login-button', 'n_clicks')]
)
def login_redirect(n_clicks):
    if n_clicks > 0:
        return '/login'
    return '/'

@server.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('samaccountname', None)
    return redirect('/')

if __name__ == '__main__':
    app.run_server(debug=True, port=8010)