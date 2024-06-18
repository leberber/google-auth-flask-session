
from dash import register_page
import dash_mantine_components as dmc
from dash import dcc
register_page(__name__, path="/")


__app__ = 'app.py'
__home__ = 'pages/home/home.py'
__analytics__ = 'pages/analytics/analytics.py'
__secret__ = 'pages/secret.py'

with open(__app__, 'r') as file:
    __app__ = file.read()
 
with open(__home__, 'r') as file:
    __home__ = file.read()

with open(__analytics__, 'r') as file:
    __analytics__ = file.read()

with open(__secret__, 'r') as file:
    __secret__ = file.read()

layout = dmc.Box(
    m=30,
    children = [
        dmc.Title("Dash App with Flask Authentication", order=2),
        dmc.Text("""This is a Dash application that integrates with Flask for user authentication, including support for OAuth with Google. The application uses the Mantine library for UI components and supports user registration, login, and logout functionality. Additionally, it includes a theme switcher and sidebar toggle implemented via client-side callbacks."""),
 
        dcc.Markdown('''
## Application Structure
- User registration and login using Flask.
- OAuth authentication with Google.
- Dynamic UI components using Dash and Dash Mantine Components
- heme switching functionality.


'''),
        dmc.Title("1. Clone the repository", order=3, pt=20),
        dmc.CodeHighlight(
            language="sh",
                code=""" 
https://github.com/leberber/google-auth-flask-session
cd google-auth-flask-session
                """,
        ),
        dmc.Title("2. install required packages", order=3, pt=20),
        dmc.CodeHighlight(
            language="sh",
                code=""" 
pip install -r requirements.txt
                """,
        ),
dmc.Title("3. Set up environment variables:", order=3, pt=20),

 dmc.Highlight("Create a .env file in the project root directory.", highlight=".env"),
 dmc.Highlight("Add the following variables to the .env file:", highlight=".env"),
        dmc.CodeHighlight(
            language="sh",
                code=""" 
SECRET_KEY=your_secret_key
CLIENT_ID=your_google_client_id
CLIENT_SECRET=your_google_client_secret
                """,
        ),
 dmc.Title("4. Run The application:", order=3, pt=20),
        dmc.CodeHighlight(
            language="sh",
                code=""" 
python app.py
                """,
        ),

dcc.Markdown('''

## Application Structure

- **`app.py`**: Main application file that sets up the Dash and Flask server, routes, and callbacks.
- **`components/header.py`**: Contains the header component for the app.
- **`components/sidebar.py`**: Contains the sidebar component for the app.
- **`utils/helpers.py`**: Utility functions used in the application.
- **`appconfig.py`**: Configuration file for external stylesheets and other settings.
- **`db.json`**: JSON file used as a simple database for storing user information.

## OAuth Authentication

To use OAuth authentication with Google, ensure you have registered your application with Google and obtained the client ID and client secret. These credentials should be added to your `.env` file as shown above.

## Routes

- **`/login`**: Handles user login via a POST request.
- **`/register`**: Handles user registration via a POST request.
- **`/signingoogle`**: Initiates Google OAuth login.
- **`/authorize`**: Handles the callback from Google after authentication.

## Callbacks

### Python Callbacks

- **`update_user_initials`**: Updates the user avatar and initials in the UI based on the current session state.

### Clientside Callbacks

- **`theme_switcher_callback`**: Toggles the theme between light and dark modes.
- **`side_bar_toggle`**: Toggles the visibility of the sidebar.

## Acknowledgments

This code is influenced by Dash community member @jinnyzor's implementation of a login system with Flask, which can be found in this discussion: [Dash App Pages with Flask Login Flow](https://community.plotly.com/t/dash-app-pages-with-flask-login-flow-using-flask/69507).

'''),
       
     
 dmc.Title("Take a look at the code here:", order=3, pt=20),

dmc.Accordion(
    value="__app_",
    multiple=True,
    children=[
        dmc.AccordionItem(
            [
                dmc.AccordionControl("app.py"),
                dmc.AccordionPanel(
                   dmc.CodeHighlight(
                    language="python",
                    code=__app__,
                )
                ),
            ],
            value="__app__",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl("home.py"),
                dmc.AccordionPanel(
                        dmc.CodeHighlight(
                    language="python",
                    code=__home__ ,
                )
                ),
            ],
            value="__home__ ",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl("analytics.py"),
                dmc.AccordionPanel(
                        dmc.CodeHighlight(
                    language="python",
                    code=__analytics__,
                )
                ),
            ],
            value="__analytics__",
        ),
            dmc.AccordionItem(
            [
                dmc.AccordionControl("secret.py"),
                dmc.AccordionPanel(
                          dmc.CodeHighlight(
                    language="python",
                    code=__secret__,
                )
                ),
            ],
            value="__secret__",
        ),
    ],
),
        dmc.Anchor(
    "Link to the Github repo",
    href="https://github.com/leberber/google-auth-flask-session",
),
    ]
)

