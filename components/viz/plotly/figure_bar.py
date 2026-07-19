"""
bar_chart.py
=====================================================

Reusable Vertical Bar Chart


----
Bar Chart digunakan untuk membandingkan nilai antar
kategori.

Contoh:
- Revenue by Region
- Sales by Product
- Patient by Department
- Inventory by Warehouse

Chart ini hanya bertanggung jawab membuat Figure.
Tidak mengambil data dari database.
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


def create_plotly_figure_bar(
    dataframe: pd.DataFrame,
    x_column: str,
    y_column: str,
    title: str,
    color_column: str | None = None,
    show_legend: bool = False
) -> Figure:
    """
    Build reusable Plotly Vertical Bar Chart.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Source dataframe.

    x_column : str
        Category axis.

    y_column : str
        Value axis.

    title : str
        Chart title.

    color_column : str | None
        Optional grouping/color dimension.

    show_legend : bool
        Display chart legend.

    Returns
    -------
    Figure
    """

    # =================================================
    # 
    #
    # Plotly Express mampu menghasilkan struktur Figure
    # dengan cepat. Selanjutnya seluruh styling dilakukan
    # melalui update_layout(), update_traces(), dan Theme.
    # =================================================

    figure = px.bar(
        data_frame=dataframe,
        x=x_column,
        y=y_column,
        color=color_column,
        title=title,
        text_auto=".2s"
    )

    # =================================================
    # 
    #
    # Label angka langsung ditampilkan agar user tidak
    # selalu bergantung pada tooltip.
    # =================================================

    figure.update_traces(

        textposition="outside",

        hovertemplate=(
            "<b>%{x}</b><br>"
            + y_column
            + ": %{y:,.0f}"
            + "<extra></extra>"
        )

    )

    # =================================================
    # 
    #
    # Legend hanya ditampilkan jika memang diperlukan.
    # Untuk single series biasanya hanya memenuhi ruang.
    # =================================================

    figure.update_layout(

        showlegend=show_legend

    )

    # =================================================
    # Apply Corporate Theme
    # =================================================

    figure = apply_default_theme(figure)

    return figure