"""
Patient Visit Repository (DuckDB)
=====================================================
"""

from pathlib import Path

from repository.service_duckdb import service_query

# =====================================================

# SQL

# =====================================================

sql_patient_visit = """ 
    SELECT *
    FROM patient_visit_dummy
"""

sql_monthly_visit = """

    SELECT
        Month,
        SUM(Revenue) Revenue
    FROM patient_visit_dummy
    GROUP BY Month
    ORDER BY Month

"""


# =====================================================

# Repository

# =====================================================

def repo_get_summary():
    return service_query(sql_patient_visit)



def repo_get_monthly():
    return service_query(sql_monthly_visit)
