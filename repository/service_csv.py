"""
CSV Helper
=====================================================
"""

import pandas as pd
import csv


# =====================================================
# Public Function
# =====================================================

def service_csv_filepath(filepath, separator, decimal):

    with open(filepath, "r", encoding="utf-8") as file:

        sample = file.read(1024)

        try:

            dialect = csv.Sniffer().sniff(sample)
            separator = dialect.delimiter

        except csv.Error:

            separator = ","

    return pd.read_csv(
        filepath,
        sep=separator,
        decimal=decimal
    )