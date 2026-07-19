"""
Main Application

File utama untuk menjalankan
Morula Dashboard.

source .venv/bin/activate
"""

from dash import Dash, html, page_container, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import callbacks.developer.viz_library

from components.navigation.sidebar import create_sidebar
from components.navigation.navbar import create_navbar
import callbacks.navigation




# ----------------------------------------------------
# Inisialisasi Dash Application
# ----------------------------------------------------
app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dmc.styles.ALL
    ]
)

# ----------------------------------------------------
# Layout Utama
#
# Struktur:
#
# Navbar
# ├── Sidebar
# └── Page Content
# ----------------------------------------------------
app.layout = dmc.MantineProvider(
    forceColorScheme="light",
    children=[
        dcc.Location(
            id="url",
            refresh=False
        ),

        create_navbar(),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            page_container,
                            width=12
                        )
                    ]
                )
            ],
            fluid=True
        )

    ]
)


# ----------------------------------------------------
# Entry Point
# ----------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)