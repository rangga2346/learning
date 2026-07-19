"""
figure_bar_stacked.py
=====================================================

Reusable Stacked Bar Chart

WHY
----
Stacked Bar Chart digunakan untuk menampilkan
total nilai sekaligus komposisi tiap kategori.

Business Use Case
-----------------
- Patient Type Composition
- Revenue by Department
- Claim Status
- Product Composition

Known Limitation
----------------
- Sulit membandingkan nilai antar kategori selain
  kategori pertama.
- Tidak cocok jika color category terlalu banyak.
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

def create_plotly_figure_bar_stacked(

    dataframe: pd.DataFrame,

    x_column: str,

    y_column: str,

    color_column: str,

    title: str,

    show_data_label: bool = False,

    show_legend: bool = True

) -> Figure:

    """
    Build reusable Plotly Stacked Bar Chart.
    """

    # =================================================
    # Build Figure
    # =================================================

    figure = px.bar(

        data_frame=dataframe,

        x=x_column,

        y=y_column,

        color=color_column,

        barmode="stack",

        title=title,

        text_auto=".2s" if show_data_label else False

    )

    # =================================================
    # Trace Configuration
    # =================================================

    figure.update_traces(

        hovertemplate=(

            "<b>%{x}</b><br>"

            + color_column
            + ": %{fullData.name}<br>"

            + y_column
            + ": %{y:,.0f}"

            + "<extra></extra>"

        )

    )

    # =================================================
    # Layout Configuration
    # =================================================

    figure.update_layout(

        showlegend=show_legend,

        hovermode="x unified"

    )

    # =================================================
    # Corporate Theme
    # =================================================

    figure = apply_default_theme(

        figure

    )

    return figure