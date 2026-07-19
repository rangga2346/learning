"""
figure_scatter.py
=====================================================

Reusable Scatter Plot

WHY
----
Scatter Plot digunakan untuk melihat hubungan
antara dua variabel numerik.

Business Use Case
-----------------
- Revenue vs Patient Count
- Cost vs Revenue
- Waiting Time vs Satisfaction

Known Limitation
----------------
- Tidak cocok untuk data kategori murni.
- Semakin banyak titik, semakin sulit dibaca.
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


def create_plotly_figure_scatter(

    dataframe: pd.DataFrame,

    x_column: str,

    y_column: str,

    title: str,

    color_column: str | None = None,

    size_column: str | None = None,

    hover_name: str | None = None,

    show_legend: bool = True

) -> Figure:

    """
    Build reusable Scatter Plot.
    """

    # =================================================
    # Build Figure
    # =================================================

    figure = px.scatter(

        data_frame=dataframe,

        x=x_column,

        y=y_column,

        color=color_column,

        size=size_column,

        hover_name=hover_name,

        title=title

    )

    # =================================================
    # Trace Configuration
    # =================================================

    figure.update_traces(

        marker=dict(

            size=14,

            line=dict(

                width=1,

                color="white"

            )

        ),

        hovertemplate=(

            "<b>%{hovertext}</b><br>"

            + x_column
            + ": %{x:,.0f}<br>"

            + y_column
            + ": %{y:,.0f}"

            + "<extra></extra>"

        )

    )

    # =================================================
    # Layout
    # =================================================

    figure.update_layout(

        showlegend=show_legend

    )

    # =================================================
    # Theme
    # =================================================

    figure = apply_default_theme(

        figure

    )

    return figure