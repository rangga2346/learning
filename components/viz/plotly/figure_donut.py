"""
figure_donut.py
=====================================================

Reusable Donut Chart

WHY
----
Donut Chart digunakan untuk menampilkan
komposisi data.

Business Use Case
-----------------
- Patient Type
- Gender
- Payment Method
- Claim Status

Known Limitation
----------------
- Maksimal sekitar 5-6 kategori.
- Tidak cocok untuk membandingkan nilai yang sangat mirip.
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


# =====================================================
# Public Function
# =====================================================

def create_plotly_figure_donut(

    dataframe: pd.DataFrame,

    names_column: str,

    values_column: str,

    title: str,

    show_legend: bool = True

) -> Figure:

    """
    Build reusable Donut Chart.
    """

    # =================================================
    # Build Figure
    # =================================================

    figure = px.pie(

        data_frame=dataframe,

        names=names_column,

        values=values_column,

        hole=0.55,

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
    # Layout
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