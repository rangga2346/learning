"""
worksheet.py
=====================================================

Reusable Worksheet Component

WHY
----
Worksheet adalah pembungkus standar untuk
seluruh visualisasi dashboard.

Developer cukup fokus pada Figure.

Framework akan menangani:

- Bootstrap Card
- Bootstrap Card Body
- Graph
- Default Config
- Default Height
"""

# =====================================================
# Third Party Library
# =====================================================

from dash import dcc
import dash_bootstrap_components as dbc


# =====================================================
# Public Function
# =====================================================

def create_worksheet(
    id,
    figure,
    width=12,
    height=350,
    card_class="",
    graph_style=None,
    graph_config=None

):

    """
    Membuat worksheet dashboard.

    Parameters
    ----------
    figure

        Plotly Figure.

    width

        Bootstrap column width.

    height

        Default tinggi chart.

    card_class

        Tambahan CSS class.

    graph_style

        Override style Graph.

    graph_config

        Override config Graph.
    """

    # ----------------------------------------------
    # Default Graph Style
    # ----------------------------------------------

    default_style = {
        "height": f"{height}px"
    }

    # Override jika ada style custom

    if graph_style:
        default_style.update(graph_style)


    # ----------------------------------------------
    # Default Graph Config
    # ----------------------------------------------

    default_config = {
        "responsive": True,
        "displaylogo": False
    }

    if graph_config:
        default_config.update(graph_config)

    # ----------------------------------------------
    # Return Worksheet
    # ----------------------------------------------

    return dbc.Col(
        dbc.Card(
            dbc.CardBody(
                dcc.Graph(
                    id=id,
                    figure=figure,
                    style=default_style,
                    config=default_config
                )
            ),
            className=f"worksheet-card {card_class}"
        ),
        width=width
    )