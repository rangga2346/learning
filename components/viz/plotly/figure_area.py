"""
figure_area.py
=====================================================

Reusable Area Chart

WHY
----
Area Chart digunakan untuk menampilkan trend
dengan penekanan pada volume.

Business Use Case
-----------------
- Patient Visit Trend
- Revenue Trend
- Claim Trend

Known Limitation
----------------
- Tidak cocok jika memiliki terlalu banyak series.
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


def create_plotly_figure_area(

    dataframe: pd.DataFrame,

    x_column: str,

    y_column: str,

    title: str,

    color_column: str | None = None,

    show_legend: bool = False

) -> Figure:

    """
    Build reusable Area Chart.
    """

    # =================================================
    # Build Figure
    # =================================================

    figure = px.area(

        data_frame=dataframe,

        x=x_column,

        y=y_column,

        color=color_column,

        title=title

    )

    # =================================================
    # Trace Configuration
    # =================================================

    figure.update_traces(

        hovertemplate=(

            "<b>%{x}</b><br>"

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
    # Apply Theme
    # =================================================

    figure = apply_default_theme(

        figure

    )

    return figure