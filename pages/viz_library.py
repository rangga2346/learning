"""
Home Page

Halaman utama dashboard.
"""

# -------------------------------
# Import Plotly function
# -------------------------------
import dash
from dash import html, register_page, dcc
import dash_bootstrap_components as dbc

from components.cards.kpi_card import create_kpi_card
from repository.repo_patient_visit_csv import *

from components.worksheet.worksheet import create_worksheet
from components.filters.dropdown import create_dropdown_filter
from components.filters.date_range import create_date_range_filter
from utils.ids import filter as filter_id
from components.viz.plotly.figure_line import create_plotly_figure_line
from components.viz.plotly.figure_bar import create_plotly_figure_bar
from components.viz.plotly.figure_bar_horizontal import create_plotly_figure_bar_h
from components.viz.plotly.figure_bar_grouped import create_plotly_figure_bar_grouped
from components.viz.plotly.figure_bar_stacked import create_plotly_figure_bar_stacked
from components.viz.plotly.figure_donut import create_plotly_figure_donut
from components.viz.plotly.figure_pie import create_plotly_figure_pie
from components.viz.plotly.figure_treemap import create_plotly_figure_treemap
from components.viz.plotly.figure_scatter import create_plotly_figure_scatter
from components.viz.plotly.figure_area import create_plotly_figure_area
from components.viz.plotly.figure_histogram import create_plotly_figure_histogram
from components.viz.plotly.figure_combo_bar_line import create_plotly_figure_combo_bar_line
from components.viz.plotly.figure_box import create_plotly_figure_box
from components.viz.plotly.figure_gauge import create_plotly_figure_gauge
from components.viz.plotly.figure_map_scatter import create_plotly_figure_map_scatter



# -------------------------------
# Register Page
# -------------------------------
dash.register_page(
    __name__,
    path="/viz-library",
    name="Viz Library"
)

# -------------------------------
# Data - dataframe 
# -------------------------------

df_patient_visit = repo_get_summary()
df_month_revenue = repo_get_month_revenue()
default_start_date = df_patient_visit["Visit Date"].min()
default_end_date   = df_patient_visit["Visit Date"].max()


# -------------------------------
# Figure 1 - Line Chart 
# -------------------------------
home_line_month_revenue = create_plotly_figure_line(
    dataframe=df_month_revenue,
    x_column="Month",
    y_column="Revenue",
    title="Line Chart"
)

# -------------------------------
# Figure 2 - Bar Chart 
# -------------------------------
home_bar_month_revenue = create_plotly_figure_bar(
    dataframe=df_month_revenue,
    x_column="Month",
    y_column="Revenue",
    title="Bar Chart"
)

# -------------------------------
# Figure 3 - Bar Chart Horizontal 
# -------------------------------
home_bar_horizontal_revenue = create_plotly_figure_bar_h(
    dataframe=df_month_revenue,
    x_column="Revenue",
    y_column="Month",
    title="HorizontalBar Chart"
)

# -------------------------------
# Figure 4 - Bar Chart Grouped 
# -------------------------------
df_bar_month_patient_count_patient_type = repo_get_month_patient_count_patient_type()
home_bar_rev_by_patient_type = create_plotly_figure_bar_grouped(
    dataframe=df_bar_month_patient_count_patient_type,
    x_column="Patient Count",
    y_column="Month",
    title="Grouped Bar Chart",
    color_column="Patient Type"
)


# -------------------------------
# Figure 5 - Bar Chart Stacked 
# -------------------------------
home_bar_stacked_by_patient_type = create_plotly_figure_bar_stacked(
    dataframe=df_bar_month_patient_count_patient_type,
    x_column="Month",
    y_column="Patient Count",
    title="Stacked Bar Chart",
    color_column="Patient Type"
)

# -------------------------------
# Figure 6 - Donut Chart  
# -------------------------------
df_patient_type_patient_count = repo_get_patient_type_patient_count()
home_donut_by_patient_count = create_plotly_figure_donut(
    dataframe=df_patient_type_patient_count,
    names_column="Patient Type",
    values_column="Patient Count",
    title="Donut Chart"
)

# -------------------------------
# Figure 7 - Pie Chart  
# -------------------------------
home_pie_by_patient_count = create_plotly_figure_pie(
    dataframe=df_patient_type_patient_count,
    names_column="Patient Type",
    values_column="Patient Count",
    title="Pie Chart"
)

# -------------------------------
# Figure 8 - Treemap Chart  
# -------------------------------
df_hospital_department_revenue = repo_get_hospital_department_revenue()
home_treemap_revenue = create_plotly_figure_treemap(
    dataframe = df_hospital_department_revenue,
    hierarchy_columns = [ "Hospital", "Department"],
    values_column = "Revenue",
    title = "Treemap Chart"
)


# -------------------------------
# Figure 10 - Scatter Chart  
# -------------------------------
df_hospital_patient_count_revenue = repo_get_hospital_patient_count_revenue()
home_scatter_patient_count = create_plotly_figure_scatter(
    dataframe = df_hospital_patient_count_revenue,
    x_column="Patient Count",
    y_column="Revenue",
    title="Scatter Chart",
    hover_name="Hospital",
    color_column="Hospital",
    size_column="Patient Count"
)

# -------------------------------
# Figure 9 - Area Chart  
# -------------------------------
df_month_hospital_patient_count = repo_get_month_hospital_patient_count()
home_area_patient_count= create_plotly_figure_area(
    dataframe = df_month_hospital_patient_count,
    x_column="Month",
    y_column="Patient Count",
    title="Area Chart",
    color_column = "Hospital"
)

# -------------------------------
# Figure 11 - Histogram Chart  
# -------------------------------
home_hist_patient_visit = create_plotly_figure_histogram(
    dataframe = df_patient_visit,
    x_column="Patient Age",
    title="Histogram Chart",
    number_of_bins = 8
)

# -------------------------------
# Figure 12 - Combo Chart  
# -------------------------------
df_month_revenue_target_revenue =  repo_get_month_revenue_target_revenue()
home_combo_revenue_target = create_plotly_figure_combo_bar_line(
    dataframe = df_month_revenue_target_revenue,
    x_column="Month",
    bar_column="Revenue",
    line_column = "Target Revenue",
    title = "Combo Chart"
)

# -------------------------------
# Figure 13 - boxplot Chart  
# -------------------------------
home_boxplot_age_hospital = create_plotly_figure_box(
    dataframe = df_patient_visit,
    x_column="Hospital",
    y_column="Patient Age",
    title = "Boxplot Chart"
)

# -------------------------------
# Figure 14 - Gauge Chart  
# -------------------------------
home_gauge = create_plotly_figure_gauge(
    value = 87,
    title = "Gauge Chart"
)

# -------------------------------
# Figure 15 - Map Scatter Chart  
# -------------------------------
df_map = repo_get_map()
figure_map_scatter = create_plotly_figure_map_scatter(
    dataframe=df_map,
    latitude_column="Latitude",
    longitude_column="Longitude",
    hover_name="Hospital",
    title="Map Scatter Chart"   
)

figure_map_scatter.update_layout( height = 600 )

# -------------------------------
# Filter Hardcode- Hospital
# -------------------------------

# hospital_filter = create_dropdown_filter_hardcode(
#     id="hospital-filter",
#     label="Hospital (hardcode filter value)",
#     options=[
#         {
#             "label":"Morula Jakarta",
#             "value":"Jakarta"
#         },
#         {
#             "label":"Morula Bandung",
#             "value":"Bandung"
#         }
#     ]
# )

# -------------------------------
# Filter - dari dataframe
# -------------------------------

home_filter_hospital = create_dropdown_filter(
    id="home_filter_hospital",
    label="Hospital",
    dataframe=df_patient_visit,
    column="Hospital"
)

home_filter_department = create_dropdown_filter(
    id="home_filter_department",
    label="Department",
    dataframe=df_patient_visit,
    column="Department"
)

home_filter_patient_type = create_dropdown_filter(
    id="home_filter_patient_type",
    label="Patient Type (multiple)",
    dataframe=df_patient_visit,
    column="Patient Type",
    multi=True #MULTIPLE VALUE/SELECT
)

home_filter_date_range_visit = create_date_range_filter(
    id="home_filter_date_range_visit",
    label="Visit Date",
    start_date=default_start_date,
    end_date=default_end_date
)


# -------------------------------
# Layout
# -------------------------------
layout = html.Div(

    className="page-content",

    children=[

        dbc.Container(
    [
        html.Br(),
        #FILTER 
        dbc.Row(
            [ 
                dbc.Col(home_filter_hospital, width=2), 
                dbc.Col(home_filter_department, width=2),
                dbc.Col(home_filter_patient_type, width=2),
                dbc.Col(home_filter_date_range_visit, width=4),
                # BUTTON APPLY FILTER
                dbc.Col(
                    dbc.Button(
                        "Apply",
                        id="home-button-filter-apply",
                         className="filter-button"
                    ),
                    width="auto",
                    className="d-flex align-items-end"
                   
                )
            ],
            className="g-4 mb-4"
        ),
    
        dbc.Row(
            [
                 dbc.Col(
                    create_kpi_card(
                        "Patient",
                        "5,245"
                    ),
                    width=3
                ),

                dbc.Col(
                    create_kpi_card(
                        "Appointment",
                        "3,200"
                    ),
                    width=3
                ),
            ]
             ,className="mb-4"
        ),

        dbc.Row(
            [   
                # Figure 15
                create_worksheet(
                    id="figure_map_scatter", 
                    figure=figure_map_scatter, 
                    width=6,
                    height=400
                ),
                # Figure 1
                create_worksheet(
                    id="home_line_revenue_bulanan", 
                    figure=home_line_month_revenue, 
                    width=6
                ),
            ]
             ,className="mb-4"
        ),

        dbc.Row(
            [
                
                # Figure 14
                create_worksheet(
                    id="home_gauge", 
                    figure=home_gauge,
                    width=4
                ),
                #Figure 2
                create_worksheet(
                    id="home_bar_revenue_bulanan",
                    figure=home_bar_month_revenue,
                    width=8
                )
            ] ,className="mb-4"
        ),

        dbc.Row(
            [
                #Figure 3
                create_worksheet(
                    id="home_bar_horizontal_revenue",
                    figure=home_bar_horizontal_revenue, 
                    width=6
                ),
                #Figure 4
                create_worksheet(
                    id="home_bar_rev_by_patient_type",
                    figure=home_bar_rev_by_patient_type, 
                    width=6
                )
            ]
             ,className="mb-4"
        ),

        dbc.Row(
            [
                #Figure 5
                create_worksheet(
                    id="home_bar_stacked_by_patient_type",
                    figure=home_bar_stacked_by_patient_type, 
                    width=8
                ),
                #Figure 6
                create_worksheet(
                    id="home_donut_by_patient_count",
                    figure=home_donut_by_patient_count, 
                    width=4
                )
            ]
             ,className="mb-4"
        ),

        dbc.Row(
            [
                #Figure 7
                create_worksheet(
                    id="home_pie_by_patient_count",
                    figure=home_pie_by_patient_count, 
                    width=4
                ),
                #Figure 8 (treemap)
                create_worksheet(
                    id="home_treemap_revenue",
                    figure=home_treemap_revenue, 
                    width=8
                )
            ]
             ,className="mb-4"
        ),

        dbc.Row(
            [
                #Figure 9
                create_worksheet(
                    id="home_area_patient_count",
                    figure=home_area_patient_count, 
                    width=6
                ),
                #Figure 10
                create_worksheet(
                    id="home_scatter_patient_count",
                    figure=home_scatter_patient_count, 
                    width=6
                )
            ]
             ,className="mb-4"
        ),

         dbc.Row(
            [
                #Figure 11
                create_worksheet(
                    id="home_hist_patient_visit",
                    figure=home_hist_patient_visit, 
                    width=4
                ),
                #Figure 12
                create_worksheet(
                    id="home_combo_revenue_target",
                    figure=home_combo_revenue_target, 
                    width=8
                )
            ]
             ,className="mb-4"
         ),
        
        dbc.Row(
            [
                #Figure 13
                create_worksheet(
                    id="home_boxplot_age_hospital",
                    figure=home_boxplot_age_hospital, 
                    width=4
                )
            ]
            ,className="mb-4"

        )

    ],

    fluid=False, className = "dashboard-container"

)
    ]
)