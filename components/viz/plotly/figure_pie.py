"""
figure_pie.py
=====================================================

Reusable Pie Chart

WHY
----
Pie Chart digunakan untuk menampilkan proporsi
suatu kategori terhadap total.

Business Use Case
-----------------
- Payment Method
- Gender
- Patient Type
- Claim Status

Known Limitation
----------------
- Maksimal 5-6 kategori.
- Tidak cocok untuk membandingkan nilai yang mirip.
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


def create_plotly_figure_pie(

    dataframe: pd.DataFrame,

    names_column: str,

    values_column: str,

    title: str,

    show_legend: bool = True

) -> Figure:

    """
    Build reusable Pie Chart.
    """

    # =================================================
    # Build Figure
    # =================================================

    figure = px.pie(

        data_frame=dataframe,

        names=names_column,

        values=values_column,

        title=title

    )

    # =================================================
    # Trace Configuration
    # =================================================

    figure.update_traces(

        textposition="inside",

        textinfo="percent+label",

        hovertemplate=(

            "<b>%{label}</b><br>"

            + values_column
            + ": %{value:,.0f}<br>"

            + "Percentage: %{percent}"

            + "<extra></extra>"

        )

    )

    # =================================================
    # Layout Configuration
    # =================================================

    figure.update_layout(

        showlegend=show_legend

    )

    # =================================================
    # Corporate Theme
    # =================================================

    figure = apply_default_theme(

        figure

    )

    return figure