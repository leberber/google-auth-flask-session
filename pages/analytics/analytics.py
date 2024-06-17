from dash import  ( 
    Output, Input, callback, clientside_callback, ClientsideFunction,
    register_page, dcc
)
import dash_mantine_components as dmc
from utils.helpers import iconify
from data import emissions

register_page(__name__, path="/analytics")


layout = dmc.Box(
    children = [
        dcc.Store(id = 'HighchartsSampleData', data=emissions ),
        dmc.Paper(
            className = 'ChartAreaDiv',
            shadow="sm",
            children = [
                dmc.Box(id = 'highchartAreaChart'),
                dmc.Center(
                    children = [
                        dmc.Text("Filter Out A region", p = 20),
                        dmc.SegmentedControl(
                            id="selectRegion",
                            value="null",
                            data=['Europe','Africa','Oceania','North America','South America','Asia'],
                        ),
                        dmc.Button(
                            "Reset",
                            id = 'resetHighChart',
                            variant="subtle",
                            rightSection=iconify(icon="system-uicons:reset"),
                            color="blue",
                        ),
                    ]
                )
            ]
        )  
    ]
)

clientside_callback(
    ClientsideFunction(
        namespace='highcharts',
        function_name='packedbubble'
    ),
 Output("highchartAreaChart", "children"),
 Input("HighchartsSampleData", "data"),
 Input("resetHighChart", "n_clicks"),
 

)

