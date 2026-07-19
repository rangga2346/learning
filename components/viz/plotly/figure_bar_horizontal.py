"""
figure_bar_horizontal.py
=====================================================

Reusable Horizontal Bar Chart

WHY
----
Horizontal Bar Chart digunakan ketika label kategori
cukup panjang atau dashboard menampilkan ranking.

Contoh:
- Top 10 Customer
- Top 10 Product
- Revenue by Region
- Sales by Branch
"""

# ====================================================
# Third Party Library
# ====================================================

import pandas as pd
import plotly.express as px

from plotly.graph_objects import Figure

# ====================================================
# Internal Project
# ====================================================

from components.viz.plotly.theme import apply_default_theme


# ====================================================
# Public Function
# ====================================================

def create_plotly_figure_bar_h(
    dataframe: pd.DataFrame,
    x_column: str,
    y_column: str,
    title: str,
    color_column: str | None = None,
    show_legend: bool =False
) -> Figure:

    """
    Build reusable Horizontal Bar Chart.
    """

    # ===============================================
    # WHY
    #
    # Orientation "h" membuat kategori berada di
    # sumbu Y sehingga nama kategori yang panjang
    # tetap mudah dibaca.
    # ===============================================

    figure = px.bar(

        data_frame=dataframe,

        x=x_column,

        y=y_column,

        color=color_column,

       # horizontal
        orientation="h",

        title=title,

        text_auto=".2s"

    )

    # ===============================================
    # Trace
    # ===============================================

    figure.update_traces(

        textposition="outside",

        hovertemplate=(

            "<b>%{y}</b><br>"

            + x_column

            + ": %{x:,.0f}"

            + "<extra></extra>"

        )

    )

    # ===============================================
    # Layout
    # ===============================================

    figure.update_layout(

        showlegend=show_legend

    )

    # ===============================================
    # Theme
    # ===============================================

    figure = apply_default_theme(

        figure

    )

    return figure