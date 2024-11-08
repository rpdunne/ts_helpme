import pytest
from tshelpme import helper
import pandas as pd


@pytest.mark.parametrize('start, end', [
    pytest.param('2022-01-02', None, id='change start date'), 
    pytest.param('2022-01-07', '2022-01-08', id='start & end date'), 

    # pytest.param()
])
def test_filter_by_time(start, end):
    # arrange
    periods = 10
    df = pd.DataFrame({
        "time": pd.date_range("2022-01-01", periods=periods, freq="D"),
        "value": list(range(periods))
    })
    # act
    df_result = helper.filter_by_time(df, start=start, end=end)

    # assert
    if end:
        assert df_result['time'].max() == pd.Timestamp(end)
    if start:
        assert df_result['time'].min() == pd.Timestamp(start)