from dash import html
import dash_mantine_components as dmc


def create_date_range_filter(
    id,
    label,
    start_date=None,
    end_date=None,
):

    return html.Div(

        [

            html.Label(
                label,
                className="filter-label"
            ),

            html.Div(

                [

                    html.Div(
                        "📅",
                        className="glass-date-icon"
                    ),

                    dmc.DatePickerInput(

                        id=f"{id}_start",

                        value=start_date,

                        clearable=False,

                        variant="unstyled",

                        valueFormat="DD MMM YYYY",

                        className="glass-date-input"

                    ),

                    html.Div(
                        className="glass-divider"
                    ),

                    html.Div(
                        "→",
                        className="glass-arrow"
                    ),

                    html.Div(
                        className="glass-divider"
                    ),

                    dmc.DatePickerInput(

                        id=f"{id}_end",

                        value=end_date,

                        clearable=True,

                        variant="unstyled",

                        valueFormat="DD MMM YYYY",

                        className="glass-date-input"

                    )

                ],

                className="glass-date-range"

            )

        ]

    )