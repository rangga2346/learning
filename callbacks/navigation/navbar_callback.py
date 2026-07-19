"""
=====================================================
Navbar Callback
=====================================================

Mengubah menu aktif berdasarkan URL.
"""

from dash import Input, Output, callback


@callback(
    Output("nav-home", "className"),
    Output("nav-viz-library", "className"),
    Input("url", "pathname"),
)
def update_navbar(pathname):

    home = "nav-link"
    developer = "nav-link"

    if pathname == "/":
        home = "nav-link active"

    elif pathname.startswith("/viz-library"):
        developer = "nav-link active"
    
    return home, developer