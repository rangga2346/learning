"""
figure_bar_grouped.py
=====================================================

Reusable Grouped Bar Chart


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

def create_plotly_figure_bar_grouped(
    dataframe: pd.DataFrame,
    x_column: str,
    y_column: str,
    title: str,
    color_column: str,
    show_data_label: bool = True,
    show_legend: bool = True
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

       # mode group
        barmode="group",

        title=title,

        text_auto=".2s" if show_data_label else False,

    )

    # ===============================================
    # Trace
    # ===============================================

    figure.update_traces(

        textposition="outside",

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


"""
Known Limitation
----------------
- Tidak cocok jika jumlah kategori pada color_column terlalu banyak
  (>5), karena legend akan sulit dibaca.
- Label data dapat saling bertabrakan jika nilai antar bar berdekatan.
"""