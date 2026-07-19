"""
figure_combo_bar_line
=====================================================

Reusable Combo Chart

----
Menampilkan dua measure berbeda
dalam satu visualisasi.

Business Use Case
-----------------
- Revenue vs Target
- Revenue vs Growth
- Patient vs Capacity

Known Limitation
----------------
- Maksimal dua Y Axis.
"""

import pandas as pd

import plotly.graph_objects as go

from plotly.graph_objects import Figure

from components.viz.plotly.theme import apply_default_theme

def create_plotly_figure_combo_bar_line(

    dataframe: pd.DataFrame,

    x_column: str,

    bar_column: str,

    line_column: str,

    title: str,

    show_legend: bool = True

) -> Figure:

    # =================================================
    # Build Figure
    # =================================================
    figure = go.Figure()

    figure.add_bar(

        x=dataframe[x_column],

        y=dataframe[bar_column],

        name=bar_column

    )

    # =================================================
    # Trace Configuration
    # =================================================
    figure.add_scatter(

        x=dataframe[x_column],

        y=dataframe[line_column],

        mode="lines+markers",

        name=line_column

    )

    # =================================================
    # Layout Configuration
    # =================================================
    figure.update_layout(

        title=title,

        showlegend=show_legend,

        hovermode="x unified"

    )

    # =================================================
    # Apply Theme
    # =================================================
    figure = apply_default_theme(

        figure

    )


    return figure