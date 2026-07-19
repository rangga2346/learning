"""
line_chart.py
====================================================

Reusable Line Chart Component

WHY
---
Komponen ini bertanggung jawab hanya untuk membuat
visualisasi Line Chart.

Komponen ini TIDAK mengambil data dari database.

Dengan pemisahan ini:

Repository --> DataFrame --> Chart --> Dashboard

chart dapat digunakan kembali oleh seluruh halaman.
"""

# ====================================================
# Third Party Library
# ====================================================

import plotly.express as px
import pandas as pd
from plotly.graph_objects import Figure


# ====================================================
# Chart Factory
# ====================================================

def create_plotly_figure_line(
    dataframe: pd.DataFrame,
    x_column: str,
    y_column: str,
    title: str
) -> Figure:
    """
    Membuat reusable Plotly Line Chart.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Data yang akan divisualisasikan.

    x_column : str
        Nama kolom sumbu X.

    y_column : str
        Nama kolom sumbu Y.

    title : str
        Judul chart.

    Returns
    -------
    plotly.graph_objects.Figure
        Figure Plotly yang siap ditampilkan
        pada Dash.
    """

    # ==========================================
    # 
    #
    # Plotly Express dipilih karena:
    #
    # - Sintaks sederhana
    # - Cepat dikembangkan
    # - Konsisten
    #
    # Nanti ketika butuh visualisasi kompleks,
    # kita akan menggunakan Graph Objects.
    # ==========================================

    fig = px.line(
        dataframe,
        x=x_column,
        y=y_column,
        title=title
    )

    # ==========================================
    # 
    #
    # Seluruh aplikasi akan memakai theme yang
    # sama sehingga pengguna mendapatkan
    # pengalaman visual yang konsisten.
    # ==========================================

    from components.viz.plotly.theme import apply_default_theme
    fig = apply_default_theme(fig)

    return fig