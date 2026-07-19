from dash import html
import dash_bootstrap_components as dbc


def create_kpi_card(title, value):

    return dbc.Card(

        dbc.CardBody(

            [

                html.H6(title),

                html.H3(value)

            ]

        ),

        className="kpi-card"

    )