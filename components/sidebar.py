

import dash_mantine_components as dmc
from dash import dcc
from utils.helpers import iconify



sidebar = dmc.Box(
    children = [
         dmc.NavLink(
            label="Home",
            leftSection=iconify(icon="solar:home-2-line-duotone", width = 20),
            href='/'
        ),
        dmc.NavLink(
            label="Analytics",
            leftSection=iconify(icon="hugeicons:analytics-02", width = 20),
            href='/analytics'
        ),
        dmc.NavLink(
            label="Secret",
            leftSection=iconify(icon="solar:lock-keyhole-minimalistic-unlocked-line-duotone", width = 20),
            href='/secret'
        ),

        ]
    )