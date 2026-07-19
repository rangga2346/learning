"""
figure_treemap.py
=====================================================

Reusable Treemap Chart

WHY
----
Treemap digunakan untuk visualisasi data
yang memiliki struktur hierarki.

Business Use Case
-----------------
- Hospital -> Department
- Region -> Province
- Category -> Product

Known Limitation
----------------
- Tidak cocok jika terlalu banyak level hierarchy.
- Nama kategori yang terlalu panjang akan terpotong.
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


def create_plotly_figure_treemap(

    dataframe: pd.DataFrame,

    hierarchy_columns: list[str],

    values_column: str,

    title: str

) -> Figure:

    """
    Build reusable Treemap Chart.
    """

    # =================================================
    # WHY
    #
    # path menentukan level hierarchy.
    #
    # Contoh:
    #
    # Hospital
    #     └── Department
    #
    # atau
    #
    # Region
    #     └── Province
    #         └── City
    #
    # Plotly akan membuat seluruh hierarchy
    # secara otomatis.
    # =================================================

    figure = px.treemap(

        data_frame=dataframe,

        path=hierarchy_columns,

        values=values_column,

        title=title

    )

    # =================================================
    # Trace Configuration
    # =================================================

    figure.update_traces(

        textinfo="label+value+percent parent",

        hovertemplate=(

            "<b>%{label}</b><br>"

            + values_column
            + ": %{value:,.0f}<br>"

            + "Contribution: %{percentParent}"

            + "<extra></extra>"

        )

    )

    # =================================================
    # Layout
    # =================================================

    figure.update_layout(

        margin=dict(

            l=10,

            r=10,

            t=50,

            b=10

        )

    )

    # =================================================
    # Corporate Theme
    # =================================================

    figure = apply_default_theme(

        figure

    )

    return figure