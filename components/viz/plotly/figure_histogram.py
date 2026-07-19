"""
figure_histogram.py
=====================================================

Reusable Histogram

----
Histogram digunakan untuk melihat distribusi
data numerik.

Business Use Case
-----------------
- Patient Age Distribution
- Waiting Time Distribution
- Revenue Distribution

Known Limitation
----------------
- Hanya cocok untuk kolom numerik.
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


def create_plotly_figure_histogram(

    dataframe: pd.DataFrame,

    x_column: str,

    title: str,

    color_column: str | None = None,

    number_of_bins: int = 10,

    show_legend: bool = False

) -> Figure:

    """
    Build reusable Histogram.
    """

    # =================================================
    # Build Figure
    # =================================================

    figure = px.histogram(

        data_frame=dataframe,

        x=x_column,

        color=color_column,

        nbins=number_of_bins,

        title=title

    )

    # =================================================
    # Trace Configuration
    # =================================================

    figure.update_traces(

        hovertemplate=(

            "<b>Range</b>: %{x}<br>"

            + "Count: %{y}"

            + "<extra></extra>"

        )

    )

    # =================================================
    # Layout Configuration
    # =================================================

    figure.update_layout(

        showlegend=show_legend,

        bargap=0.05

    )

    # =================================================
    # Theme
    # =================================================

    figure = apply_default_theme(

        figure

    )

    return figure