"""
theme.py
====================================================

Plotly Theme Engine

WHY
----
Seluruh dashboard harus memiliki identitas visual
yang konsisten.

Dengan memusatkan konfigurasi visual di satu tempat,
perubahan branding tidak memerlukan perubahan pada
setiap chart.

Semua chart WAJIB menggunakan Theme Engine ini.
"""

# ====================================================
# Plotly
# ====================================================

import plotly.graph_objects as go


# ====================================================
# Theme Constants
# ====================================================

CORPORATE_THEME = {

    # ==========================================
    # Typography
    # ==========================================

    "font_family": "Helvetica, Arial, sans-serif",

    "font_size": 13,

    "title_color": "#2E3644",

    # ==========================================
    # Glass Background
    # ==========================================

    "paper_bgcolor": "rgba(255,255,255,0)",

    "plot_bgcolor": "rgba(255,255,255,0)",

    # ==========================================
    # Brand Color
    # ==========================================

    "primary_color": "#F59E0B",

    # ==========================================
    # Grid
    # ==========================================

    "grid_color": "rgba(120,130,160,.12)",

}


# ====================================================
# Public Function
# ====================================================

def apply_default_theme(
    figure: go.Figure
) -> go.Figure:
    """
    Menerapkan tema visual standar perusahaan.

    Parameters
    ----------
    figure : go.Figure
        Figure Plotly yang akan diberi tema.

    Returns
    -------
    go.Figure
        Figure dengan tema perusahaan.
    """

    # ==============================================
    # 
    #
    # Semua konfigurasi visual ditempatkan di sini
    # agar konsisten di seluruh dashboard.
    # ==============================================

    figure.update_layout(

        template="plotly_white",

        font=dict(

            family=CORPORATE_THEME["font_family"],

            size=CORPORATE_THEME["font_size"],

            color=CORPORATE_THEME["title_color"]

        ),

        paper_bgcolor=CORPORATE_THEME["paper_bgcolor"],

        plot_bgcolor=CORPORATE_THEME["plot_bgcolor"],

        title_font=dict(

            size=20,

            color=CORPORATE_THEME["title_color"]

        ),

        margin=dict(

            l=24,

            r=24,

            t=60,

            b=24

        ),

        legend=dict(

            bgcolor="rgba(255,255,255,0)",

            borderwidth=0

        )

    )

    # ==============================================
    # 
    #
    # Seluruh axis menggunakan warna grid yang sama
    # agar tampilan dashboard konsisten.
    # ==============================================

    figure.update_xaxes(

        gridcolor=CORPORATE_THEME["grid_color"]

    )

    figure.update_yaxes(

        gridcolor=CORPORATE_THEME["grid_color"]

    )

    return figure