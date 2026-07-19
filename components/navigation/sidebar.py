"""
sidebar.py
----------------------------------------
Reusable Sidebar Component

File ini bertanggung jawab untuk membuat
menu navigasi utama aplikasi.

Keuntungan:
- Tidak memenuhi app.py
- Dapat digunakan ulang
- Mudah dikembangkan jika menu bertambah
"""

# Import komponen HTML bawaan Dash
from dash import html

# Import Bootstrap Components
import dash_bootstrap_components as dbc


def create_sidebar():
    """
    Membuat Sidebar Navigation.

    Returns
    -------
    html.Div
        Komponen Sidebar yang siap digunakan
        pada layout utama.
    """

    return html.Div(

        [

            # ========================================
            # Judul Sidebar
            # ========================================
            html.H3(
                "Morula",
                className="text-white text-center mt-3"
            ),

            html.Hr(),

            # ========================================
            # Navigation Menu
            # ========================================
            dbc.Nav(

                [

                    dbc.NavLink(

                        "🏠 Home",

                        href="/",

                        active="exact"

                    ),

                    dbc.NavLink(

                        "📊 Sales",

                        href="/dashboard_sales",

                        active="exact"

                    ),

                    dbc.NavLink(

                        "💰 Finance",

                        href="/dashboard_finance",

                        active="exact"

                    )

                ],

                vertical=True,

                pills=True

            )

        ],

        # ========================================
        # CSS Style
        # ========================================
        className="sidebar"

    )