
import dash_mantine_components as dmc
from utils.helpers import iconify

def header():
    return dmc.Group(
            justify='space-between',
            className = 'header-inner-container',
            px = 10,
            children = [
                dmc.Burger(id="burger-button", opened=False, hiddenFrom="md"),
                dmc.Paper(
                    className = 'baylek-logo-image',
                    children = [
                        dmc.Image(src="/assets/baylek.png",  className='image-width'),
                    ]
                ),
                dmc.Flex(
                    children = [
                        dmc.Menu(
                            children = [
                                dmc.MenuTarget(
                                        dmc.Box(
                                            id='avatar-indicator',
                                            children=[]
                                            )
                                    ),
                                dmc.MenuDropdown(
                                    [
                                        dmc.MenuItem(
                                              dmc.NavLink(
                                                label="Login",
                                                href='/login',
                                                rightSection=iconify(icon="solar:login-outline", width = 20),
                                            ),
                                        ),
                                        dmc.MenuItem(
                                              dmc.NavLink(
                                                label="Register",
                                                href='/register',
                                                rightSection=iconify(icon="mdi:register-outline", width = 20),
                                            ),
                                            ),
                                        dmc.MenuItem(
                                              dmc.NavLink(
                                                label="Logout",
                                                href='/logout',
                                                rightSection=iconify(icon="hugeicons:login-01", width = 20),
                                            ),
                                        ),
                                           dmc.MenuItem(
                                              dmc.NavLink(
                                                id = 'color-scheme-toggle',
                                                n_clicks=0, 
                                                rightSection=iconify(icon="ic:baseline-light-mode",  color='100%'),
                                            ),
                                        ),
                                    ]
                                ),
                            ]
                        )
                    ]
                ) 
            ]
        )