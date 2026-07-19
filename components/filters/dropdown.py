
"""
dropdown.py
=====================================================

Reusable Dropdown Filter

WHY
----
Komponen standar untuk seluruh Dropdown
pada Morula Dashboard Framework.

Developer cukup memberikan:

- DataFrame
- Nama kolom

Framework akan otomatis membuat
dropdown options.
"""

# =====================================================
# Third Party Library
# =====================================================

from dash import html
from dash import dcc


#CONTOH FILTER HARDCODE
# def create_dropdown_filter(
#     id,
#     label,
#     options,
#     value=None,
#     placeholder="Select...",
#     multi=False,
#     clearable=True
# ):

# =====================================================
# Helper Function
# =====================================================

def build_dropdown_options(
    dataframe,
    column
):
    """
    Generate Dropdown Options
    dari DataFrame.
    """

    values = sorted(
        dataframe[column]
        .dropna()
        .unique()
    )

    options = [ {
            "label": value,
            "value": value
        } for value in values
    ]

    return options


# =====================================================
# Public Function
# =====================================================

def create_dropdown_filter(
    id,
    label,
    dataframe,
    column,
    value=None,
    placeholder="Select...",
    multi=False,
    clearable=True
):
    """
    Create Reusable Dropdown Filter.
    """

    # ---------------------------------------------
    # Generate Options
    # ---------------------------------------------

    options = build_dropdown_options(
        dataframe,
        column
    )

    # ---------------------------------------------
    # Layout
    # ---------------------------------------------

    return html.Div(
        [
            html.Label(
                label,
                className="filter-label"
            ),
            dcc.Dropdown(
                id=id,
                options=options,
                value=value,
                placeholder=placeholder,
                multi=multi,
                clearable=clearable,
                className="filter-dropdown"
            )
        ],
        className="filter-container"
    )