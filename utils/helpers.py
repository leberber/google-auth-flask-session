
from dash_iconify import DashIconify
def iconify(icon, color = 'dark', width=30, cN = '_'):
    return DashIconify(
        icon=icon,  
        color=color, 
        width = width, 
        className=cN
    )