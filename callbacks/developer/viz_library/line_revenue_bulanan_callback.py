"""
dashboard_callback.py
=====================================================
"""

from dash import Input
from dash import Output
from dash import callback
from dash import State
from repository.repo_patient_visit_duckdb import repo_get_summary 
from utils.dataframe_filter import filter_dataframe
from components.viz.plotly.figure_line import create_plotly_figure_line
from utils.dataframe_filter import ( filter_dataframe, filter_date_range )

#CALLBACK FILTER CHART LINE REVENUE BULANAN
@callback(
    Output( "home_line_revenue_bulanan", "figure"),
    Input( "home-button-filter-apply", "n_clicks"),
    State( "home_filter_department", "value"),
    State( "home_filter_hospital", "value"),
    State( "home_filter_patient_type", "value"),
    State( "home_filter_date_range_visit", "start_date"),
    State( "home_filter_date_range_visit", "end_date")
)

def home_line_revenue_bulanan_update(
    n_clicks,
    department,
    hospital,
    patient_type,
    start_date,
    end_date
):

    df = repo_get_summary()
    df = filter_dataframe( df, "Department", department)
    df = filter_dataframe( df, "Hospital",  hospital)
    df = filter_dataframe( df, "Patient Type", patient_type)
    df = filter_date_range( df, "Visit Date", start_date, end_date)

    figure = create_plotly_figure_line(
        dataframe=df,
        x_column="Month",
        y_column="Revenue",
        title="Revenue"
    )

    return figure





    