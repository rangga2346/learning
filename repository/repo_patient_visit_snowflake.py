"""
Patient Visit Repository (Snowflake)
=====================================================
"""

from repository.service_snowflake import service_query

# =====================================================

# SQL

# =====================================================
sql_patient_visit = """

    SELECT *
    FROM ANALYTICS.PATIENT_VISIT

"""



# =====================================================

# Repository

# =====================================================

def repo_get_summary():
    return service_query(sql_patient_visit)