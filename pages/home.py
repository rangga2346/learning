import dash
from dash import html
from components.navigation.navbar import create_navbar

dash.register_page(
    __name__,
    path="/",
    name="Home"
)

layout = html.Div(
        className="page-wrapper",
        children= [
            # create_navbar(),
            html.Div(
                children=[
                    html.H2("Morula Dashboard"),
                    html.P("Welcome.")
                ],
                className="page-content"
            )
        ]
    )