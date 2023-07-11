import os
import pytest

from my_package.data_processing import input_data, filter_by_name, filter_by_declination


TEST_DIR = os.path.join(os.path.dirname(__file__), 'test_data')


def test_input_data():
    # Test default pulsar.csv input
    default_df = input_data()
    assert len(default_df) == 3389

    # Test custom input by loading in the two values from the test data
    df = input_data(os.path.join(TEST_DIR, 'test_source_input.csv'))
    assert len(df) == 2
    assert df['Source Name'].iloc[0] == 'J0002+6216'
    assert df['Source Name'].iloc[1] == 'J0021-0909'
    # Test that the RA and Dec values are converted to degrees
    # Note: pytest.approx is used to compare floating point values
    assert df['RA (deg)'].iloc[0]  == pytest.approx(0.742375)
    assert df['RA (deg)'].iloc[1]  == pytest.approx(5.464458)
    assert df['Dec (deg)'].iloc[0] == pytest.approx(62.269278)
    assert df['Dec (deg)'].iloc[1] == pytest.approx(-9.166306)


def test_filter_by_name():
    # Test filtering by source name
    df = input_data(os.path.join(TEST_DIR, 'test_source_input.csv'))
    df = filter_by_name(df, ['J0002+6216'])
    assert len(df) == 1
    assert df['Source Name'].iloc[0] == 'J0002+6216'

def test_filter_by_declination():
    # Test filtering by declination
    df = input_data(os.path.join(TEST_DIR, 'test_source_input.csv'))
    df = filter_by_declination(df, 0, 90)
    assert len(df) == 1
    assert df['Source Name'].iloc[0] == 'J0002+6216'