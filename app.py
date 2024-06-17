


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
    # print(type(db), db)


server = Flask(__name__)
server.config.update(SECRET_KEY=os.getenv("SECRET_KEY"))

app = Dash(
    __name__, server=server, use_pages=True,
    external_stylesheets=stylesheets,
)

def get_user():
    user=''
    if 'email' in session:
        acount = session['email']
        user = f"{acount['firstname'][:1]}{acount['lastname'][:1]}"
        print(user)
    return user
# with server.app_context():
#     # get_user()
#     print('top')

app.layout = dmc.MantineProvider(
    id="mantine-provider",
    children = [
        dmc.AppShell(
            id="app-shell",
            navbar={ "breakpoint": "md", "collapsed": {"mobile": True}},
            children = [
                dcc.Location(id="url"),
                dmc.AppShellHeader(header('TT')),
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
            print('yes')
            session['email'] = user
            return redirect('/secret')
        else:
            return """invalid username and/or password <a href='/login'>login here</a> or register here <a href='/register'>register here</a> """

@server.route('/register', methods=['POST'])
def register_button_click():

    if request.form:

        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        user = db.get(email, None)
        if user :
            return f""" user name {user } is taken chose another one and continue <a href='/register'>register here</a> """
        else:
            db[email]= {"lastname":lastname,  "firstname":firstname, "email": email, "password":password}
            # db = json.dumps(db, indent=4)
            with open("db.json", "w") as outfile: 
                json.dump(db, outfile, indent=4)
            return redirect('/login')

@callback(
    Output('indicator', 'label'),
    Input("url", "pathname"),
)
def update_user_initials(url):
    user=''
    if 'email' in session:
        acount = session['email']
        user = f"{acount['firstname'][:1]}{acount['lastname'][:1]}"
        print(user)
    return user

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
    app.run_server(debug=True, port= 8052)

