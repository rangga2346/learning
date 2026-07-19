"""
figure_scatter_map.py
=====================================================

Reusable Scatter Map


----
Scatter Map digunakan untuk menampilkan
lokasi suatu entitas pada peta.

Business Use Case
-----------------
- Hospital Location
- Patient Distribution
- Branch Location
"""
# =====================================================
# Third Party Library
# =====================================================

from plotly.graph_objects import Figure

import plotly.graph_objects as go

import plotly.express as px

import pandas as pd

# =====================================================
# Internal Project
# =====================================================

from components.viz.plotly.theme import apply_default_theme
def create_plotly_figure_map_scatter(

    dataframe: pd.DataFrame,

    latitude_column: str,

    longitude_column: str,

    hover_name: str,

    title: str

) -> Figure:

        figure = px.scatter_map(

            data_frame=dataframe,

            lat=latitude_column,

            lon=longitude_column,

            hover_name=hover_name,

            zoom=4,

            title=title

        )

        figure.update_layout(

            map_style="open-street-map",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(

                l=0,

                r=0,

                t=40,

                b=0

            )

        )

        return figure
    