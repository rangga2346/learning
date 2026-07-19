"""
figure_bar_bullet.py
=====================================================

Reusable bullet Bar Chart

WHY
----
Chart ini digunakan untuk membandingkan komposisi
antar kategori dalam bentuk persentase.

Business Use Case
-----------------
- Patient Type Composition
- Gender Composition
- Revenue Contribution
- Payment Method
"""

# =====================================================
# Third Party Library
# =====================================================

import pandas as pd
import plotly.express as px

from plotly.graph_objects import Figure

# =====================================================
# Internal Project
# =====================================================

from components.viz.plotly.theme import apply_default_theme


def create_plotly_figure_bar_bullet(

    dataframe: pd.DataFrame,

    x_column: str,

    y_column: str,

    color_column: str,

    title: str,

    show_data_label: bool = True,

    show_legend: bool = True

) -> Figure:

    """
    Build reusable 100% Stacked Bar Chart.
    """

    # =================================================
    # 
    #
    # groupnorm="percent" akan mengubah setiap batang
    # menjadi 100% sehingga fokus user adalah komposisi.
    # =================================================

    figure = px.bar(

        data_frame=dataframe,

        x=x_column,

        y=y_column,

        color=color_column,

        title=title,

        text_auto=".1%"

    )

    figure.update_traces(

        groupnorm="percent",

        textposition="inside" if show_data_label else "none",

        hovertemplate=(

            "<b>%{x}</b><br>"

            + color_column
            + ": %{fullData.name}<br>"

            + "Percentage: %{y:.1%}"

            + "<extra></extra>"

        )

    )

    figure.update_layout(

        barmode="stack",

        showlegend=show_legend,

        hovermode="x unified",

        yaxis_tickformat=".0%"

    )

    figure = apply_default_theme(

        figure

    )

    return figure