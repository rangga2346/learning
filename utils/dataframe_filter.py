"""
dataframe_filter.py
=====================================================

Reusable DataFrame Filter

WHY
----
Menyediakan fungsi standar Helper untuk
melakukan filtering DataFrame
berdasarkan nilai dari Dashboard Filter.
"""

# =====================================================
# Public Function
# =====================================================

def filter_date_range(
    dataframe,
    column,
    start_date,
    end_date
):
    """
    Filter DataFrame berdasarkan
    rentang tanggal.
    """

    # ---------------------------------------------
    # Tidak ada tanggal dipilih
    # ---------------------------------------------

    if start_date is None or end_date is None:
        return dataframe

    # ---------------------------------------------
    # Pastikan kolom datetime
    # ---------------------------------------------

    dataframe[column] = dataframe[column].astype("datetime64[ns]")

    # ---------------------------------------------
    # Filter Date Range
    # ---------------------------------------------

    return dataframe[
        (dataframe[column] >= start_date)
        &
        (dataframe[column] <= end_date)
    ]







def filter_dataframe(
    dataframe,
    column,
    selected_value
):
    """
    Filter DataFrame berdasarkan
    nilai Dropdown.
    """

    # ---------------------------------------------
    # Tidak ada filter
    # ---------------------------------------------

    if selected_value is None:
        return dataframe

    # ---------------------------------------------
    # Multi Select
    # ---------------------------------------------

    if isinstance(selected_value, list):

        if len(selected_value) == 0:
            return dataframe

        return dataframe[
            dataframe[column].isin(selected_value)
        ]

    # ---------------------------------------------
    # Single Select
    # ---------------------------------------------

    return dataframe[
        dataframe[column] == selected_value
    ]