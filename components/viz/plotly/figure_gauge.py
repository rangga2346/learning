"""
figure_gauge.py
=====================================================

Reusable KPI Gauge

----
Gauge digunakan untuk menampilkan
tingkat pencapaian KPI.

Business Use Case
-----------------
- Revenue Achievement
- Bed Occupancy
- SLA
- Patient Satisfaction

Known Limitation
----------------
- Menampilkan satu KPI saja.
"""


# =====================================================
# Third Party Library
# =====================================================

from plotly.graph_objects import Figure

import plotly.graph_objects as go

# =====================================================
# Internal Project
# =====================================================

from components.viz.plotly.theme import apply_default_theme

def create_plotly_figure_gauge(

    value: float,

    title: str,

    minimum_value: float = 0,

    maximum_value: float = 100,

     threshold_low=50,

    threshold_medium=80,

    threshold_high=100

) -> Figure:

    figure = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=value,

            title={

                "text": title

            },

            gauge={

                "axis":{

                    "range":[

                        minimum_value,

                        maximum_value

                    ]

                },

                "bar":{

                    "color":"green"

                },

                "steps":[

                    {

                        "range":[

                            0,

                            50

                        ],

                        "color":"#ff4d4f"

                    },

                    {

                        "range":[

                            50,

                            80

                        ],

                        "color":"#faad14"

                    },

                    {

                        "range":[

                            80,

                            100

                        ],

                        "color":"#52c41a"

                    }

                ]

            }

        )

    )

    figure = apply_default_theme(

        figure

    )

    return figure