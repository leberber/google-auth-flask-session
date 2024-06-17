from dash import Dash,  html, dcc, Output,Input, callback, page_container,  ALL, ctx
import dash_mantine_components as dmc

app = Dash(
     __name__, 
     use_pages=True,  
     suppress_callback_exceptions=True,
     external_scripts=[
        'https://cdn.jsdelivr.net/npm/apexcharts',
        # These are served locally
        # 'https://code.highcharts.com/highcharts.js', 
        # 'http://code.highcharts.com/highcharts-more.js',
        'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',

        'https://d3js.org/d3.v6.min.js',
        'https://d3js.org/d3.v4.js',
        'https://d3js.org/d3-geo-projection.v2.min.js',
         {
            'src': 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',
            'integrity': 'sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="',
            'crossorigin': ''
        },
    ],
    external_stylesheets = [
        {
            'href': 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',
            'rel': 'stylesheet',
            'integrity': 'sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=',
            'crossorigin': ''
        },
    ], 
)



server = app.server

_pages = {
    'apexcharts':'https://apexcharts.com/',
    'highcharts':'https://www.highcharts.com/demo' ,
    'leaflet':'https://leafletjs.com/', 
    'd3js':'https://d3js.org/'
}

focusLinkStyle = { 
     'width':'70px', 
     'height':'70px', 
     'margin':'-20px', 
     'backgroundColor':'rgb(255, 255, 255)', 
     'borderRadius':'50%', 
     'padding':'15px', 
     'boxShadow': '0 0 50px #ccc'
}

def page_link (pageHref):
    if pageHref == 'd3js':
        href = "/"
        style = focusLinkStyle
    else:
        href = pageHref
        style = {}

    return dcc.Link(
        href= href,  
        children =[
            dmc.ActionIcon(
                id={"type": "pages-links", "index": pageHref},
                n_clicks = 0,
                style = style,
                children = [
                    dmc.Image(src=f"/assets/svg/{pageHref}.svg", width='100%')
                ]
            )
        ]
    )


def goToSite(link, logo):
    return  html.A(
                href=link, 
                target="_blank",
                children = [
                    dmc.Button(
                        "Visite Library",
                        variant="subtle",   
                        leftIcon=dmc.Image(src=f"/assets/svg/{logo}.svg", width=25),
                    )
                ]
            )

app.layout = html.Div(
    id = 'dash-app-layout',
    children = [

        html.A(
            href='https://github.com/leberber/dashJsLibraries/tree/main', 
            target="_blank",
            className = "githubLogo",
            children = [
                dmc.ActionIcon( 
                    variant="subtle",
                    children = [
                        dmc.Image(src=f"/assets/svg/github.svg", width=25), 
                    ],
                )
            ]
        ),
        html.Div(
            id = 'goToSiteButton',
            children = [ 
                 goToSite('https://d3js.org/', 'd3js')
                 
            ]
        ),
        html.Div(
            id = 'dash-page-navigation-bar',
            children = [
                page_link(p) for p in _pages
            ] 
        ),
        html.Div(
            id = 'dash-page-container',
            children = [
                page_container
            ]
        )
    ]
)

@callback(
    Output('goToSiteButton', 'children'),
    Output({'type': 'pages-links', 'index': ALL}, 'style'),
    Output({'type': 'pages-links', 'index': ALL}, 'n_clicks'),
    Input({'type': 'pages-links', 'index': ALL}, 'n_clicks'),
    prevent_initial_call = True
)
def styleCurrentPage(id):
    idx= ctx.triggered_id.index
    pageIndex = id.index(1)
    styles = [{'backgroundColor':'transparent'}] * len(id)
    styles[pageIndex] = focusLinkStyle
    
    return [ 
        goToSite(_pages[idx], idx), 
        styles, 
        [0] * len(id)
    ]



if __name__ == '__main__':
	app.run_server(
     port=8070,  debug = True
    )