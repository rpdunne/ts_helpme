import pandas as pd
from typing import Optional, Union
import datetime

TimeLike = Union[str, datetime.date, datetime.datetime, pd.Timestamp]


def filter_by_time(
    df: pd.DataFrame,
    start: Optional[TimeLike] = None,
    end: Optional[TimeLike] = None,
    *,
    inclusive: bool = True,
    time_col: str = "time",
):
    """Filter a dataframe to time range.

    Parameters:
        - df (pd.DataFrame): The dataframe to filter.
        - start: Optional start time to filter on.
        - end: Optional end time to filter on.
        - inclusive (bool): Whether filter is inclusive of end time (defaults to True).
        - time_col (str): Name of the time column.

    Returns:
        - The filtered dataframe (as a view so no copy is made)
    """
    if start:
        df = df.loc[df[time_col] >= start]
    if end and inclusive:
        df = df.loc[df[time_col] <= end]
    elif end:
        df = df.loc[df[time_col] < end]
    return df