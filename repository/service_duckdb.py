"""
DuckDB Helper
=====================================================
"""

import duckdb
import pandas as pd

# =====================================================
# Configuration
# =====================================================

DUCKDB_DATABASE_PATH = "database/morula.duckdb"




# =====================================================
# Public Function
# =====================================================

def service_query(sql: str) -> pd.DataFrame:
    """
    Execute DuckDB SQL.

    Parameters
    ----------
    sql : str

    Returns
    -------
    pandas.DataFrame
    """

    connection = duckdb.connect(
        DUCKDB_DATABASE_PATH,
        read_only=True
    )

    dataframe = connection.execute(
        sql
    ).fetchdf()

    connection.close()

    return dataframe