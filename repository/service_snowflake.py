"""
Snowflake Helper
=====================================================
"""

import os
from dotenv import load_dotenv
from snowflake.snowpark import Session
import pandas as pd


load_dotenv()
# =====================================================
# Configuration
# =====================================================
SNOWFLAKE = {
    "ACCOUNT": os.getenv("SF_ACCOUNT"),
    "USER": os.getenv("SF_USER"),
    "PASSWORD": os.getenv("SF_PASSWORD"),
    "WAREHOUSE": os.getenv("SF_WAREHOUSE"),
    "DATABASE": os.getenv("SF_DATABASE"),
    "SCHEMA": os.getenv("SF_SCHEMA"),
    "ROLE": os.getenv("SF_ROLE")
}

# =====================================================
# Public Function
# =====================================================
def service_query(sql: str) -> pd.DataFrame:
    """
    Execute Snowflake SQL.

    Parameters
    ----------
    sql : str

    Returns
    -------
    pandas.DataFrame
    """

    session = Session.builder.configs(
        SNOWFLAKE
    ).create()

    dataframe = session.sql(
        sql
    ).to_pandas()

    session.close()

    return dataframe