
"""
Patient Visit Repository (CSV)
=====================================================
"""

import pandas as pd
from repository.service_csv import service_csv_filepath

CSV_PATIENT_VISIT = "data/patient_visit_dummy_2025.csv"
DECIMAL = ","
SEPARATOR = ";"

# =====================================================
# Repository
# =====================================================
def repo_get_summary():
    """
    Get Patient Visit Summary.
    """
    df = service_csv_filepath( CSV_PATIENT_VISIT, SEPARATOR, DECIMAL )

    # ============================================
    # Cast Datatype
    # ============================================

    df = df.astype({
        "Patient Count": "int64",
        "Revenue": "float64",
        "Target Revenue": "float64",
        "Patient Age": "int64",
        "Waiting Time": "int64",
        "Length of Stay": "int64",
        "Target Achievement (%)": "float64",
        "Latitude": "float64",
        "Longitude": "float64"
    })

    df["Visit Date"] = pd.to_datetime(
        df["Visit Date"]
    )

    return df       


def repo_get_month_revenue():
    dataframe = repo_get_summary()
    dataframe = (
        dataframe
        .groupby(
            "Month",
            as_index=False
        )
        .agg(
            {
                "Revenue":"sum"
            }
        )
    )
    return dataframe


def repo_get_donut_patient():
    dataframe = repo_get_summary()
    dataframe = (
        dataframe
        .groupby(
            "Patient Type",
            as_index=False
        )
        .agg(
            {
                "Patient Count":"sum"
            }
        )
    )
    return dataframe


def repo_get_scatter():
    dataframe = repo_get_summary()
    dataframe = (
        dataframe
        .groupby(
            "Hospital",
            as_index=False
        )
        .agg(
            {
                "Revenue":"sum",
                "Patient Count":"sum"
            }
        )
    )
    return dataframe


def repo_get_month_patient_count_patient_type():
    df = repo_get_summary()
    return (
        df
        .groupby(
            ["Month","Patient Type"],
            as_index=False
        )
        .agg(
            {
                "Patient Count":"sum"
            }
        )
    )

def repo_get_patient_type_patient_count():
    df = repo_get_summary()
    return (
        df
        .groupby(
            "Patient Type",
            as_index=False
        )
        .agg(
            {
                "Patient Count":"sum"
            }
        )
    )

def repo_get_hospital_department_revenue():
    df = repo_get_summary()
    return (
        df
        .groupby(
            ["Hospital","Department"],
            as_index=False
        )
        .agg(
            {
                "Revenue":"sum"
            }
        )
    )

def repo_get_hospital_patient_count_revenue():
    df = repo_get_summary()
    return (
        df
        .groupby(
            "Hospital",
            as_index=False
        )
        .agg(
            {
                "Revenue":"sum",
                "Patient Count":"sum"
            }
        )
    )

def repo_get_month_hospital_patient_count():
    df = repo_get_summary()
    return (
        df
        .groupby(
            ["Month","Hospital"],
            as_index=False
        )
        .agg(
            {
                "Patient Count":"sum"
            }
        )
    )


def repo_get_month_revenue_target_revenue():
    dataframe = repo_get_summary()
    return (
        dataframe
        .groupby(
            "Month",
            as_index=False
        )

        .agg({
            "Revenue":"sum",
            "Target Revenue":"sum"
        })

    )


def repo_get_map():
    dataframe = repo_get_summary()
    return (
        dataframe
        .groupby(
            [
                "Hospital",
                "Latitude",
                "Longitude"
            ],
            as_index=False
        )
        .agg({
            "Revenue":"sum",
            "Patient Count":"sum"
        })
    )