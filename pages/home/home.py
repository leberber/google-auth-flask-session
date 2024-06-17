
from dash import register_page
import dash_mantine_components as dmc

register_page(__name__, path="/")


layout = dmc.Box(
    [
        'This is the honme page'
    ]
)

# restricted_page = {}

# def require_login(page):
#     for pg in dash.page_registry:
#         if page == pg:
#             restricted_page[dash.page_registry[pg]['path']] = True

# # 
# # require_login(__name__)