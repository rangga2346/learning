"""
figure_box.py
=====================================================

Reusable Box Plot

----
Box Plot digunakan untuk melihat
penyebaran data numerik sekaligus
mendeteksi outlier.

Business Use Case
-----------------
- Patient Age
- Waiting Time
- Length of Stay
- Revenue Distribution

Known Limitation
----------------
- Tidak cocok untuk jumlah data yang sangat sedikit.
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


def create_plotly_figure_box(

    dataframe: pd.DataFrame,

    y_column: str,

    title: str,

    x_column: str | None = None,

    color_column: str | None = None,

    show_points: bool = True

) -> Figure:

    """
    Build reusable Box Plot.
    """

    # =================================================
    # Build Figure
    # =================================================

    figure = px.box(

        data_frame=dataframe,

        x=x_column,

        y=y_column,

        color=color_column,

        points="outliers" if show_points else False,

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
    # Layout
    # =================================================

    figure.update_layout(

        hovermode="closest"

    )

    # =================================================
    # Theme
    # =================================================

    figure = apply_default_theme(

        figure

    )

    return figure