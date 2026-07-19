
"""
database.py
=====================================================

DuckDB Connection Helper

WHY
----
Seluruh repository menggunakan
connection yang sama.

Apabila nanti migrasi ke Snowflake,
perubahan hanya terjadi di file ini.
"""

# =====================================================
# Third Party Library
# =====================================================

import duckdb


# =====================================================
# Connection
# =====================================================

DATABASE_PATH = "database/morula.duckdb"


# =====================================================
# Public Function
# =====================================================

def get_connection():
    """
    Return DuckDB Connection.
    """

    return duckdb.connect(
        DATABASE_PATH,
        read_only=True
    )