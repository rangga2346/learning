"""
=====================================================
Top Navigation Bar
=====================================================

Reusable Floating Navigation Bar

WHY
----
Digunakan oleh seluruh Dashboard Morula.

Ke depan akan mendukung:

- Multi Dashboard
- Notification
- User Login
- Search
- Theme Switch
"""

# =====================================================
# Dash
# =====================================================

from dash import html, dcc

# =====================================================
# Configuration
# =====================================================

from config.settings import APP_TITLE


# =====================================================
# Public Component
# =====================================================



def create_navbar():
    """
    Floating Navbar
    """

    return html.Div(

        className="navbar-wrapper",

        children=[
            html.Header(
                className="navbar",
                children=[

                    # LEFT
                    html.Div(
                        className="navbar-left",
                        children=[
                            dcc.Link(
                                html.Img(
                                    src="/assets/images/logo.svg",
                                    className="navbar-logo-image"
                                ),
                                href="/"
                            )
                        ]
                    ),

                    # CENTER
                    html.Nav(
                        className="navbar-center",
                        children=[

                            dcc.Link(
                                "Dashboard Home",
                                href="/",
                                id="nav-home",
                                className="nav-link"
                            ),

                            dcc.Link(
                                "Chart Library",
                                href="/viz-library",
                                id="nav-viz-library",
                                className="nav-link"
                            ),

                        ]
                    ),

                    # RIGHT
                    # RIGHT
                    html.Div(
                        className="navbar-right",
                        children=[
                            html.Div(
                                className="navbar-actions",
                                    children=[
                                        html.Button(
                                           html.I(className="fa-solid fa-magnifying-glass"),
                                            className="nav-icon-btn"
                                        ),
                                        html.Button(
                                           html.I(className="fa-regular fa-bell"),
                                            className="nav-icon-btn"
                                        ),
                                        html.Button(
                                           html.I(className="fa-regular fa-circle-user"),
                                            className="nav-icon-btn"
                                        ),
                                    ]
                                )
                            ]
                        )

                ]
            )

        ]

    )