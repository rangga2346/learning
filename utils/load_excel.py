"""
load_excel.py
=====================================================

Import Excel ke DuckDB

WHY
----
Mengubah source Excel menjadi
table DuckDB.
"""

# =====================================================
# Third Party Library
# =====================================================

import pandas as pd

from utils.database import get_connection


# =====================================================
# Load Excel
# =====================================================

DATAFRAME = pd.read_excel(
    "data/patient_visit.xlsx"
)

connection = get_connection()

connection.execute(
    """
    CREATE OR REPLACE TABLE patient_visit
    AS
    SELECT *
    FROM DATAFRAME
    """
)

connection.close()

print(
    "patient_visit imported successfully."
)