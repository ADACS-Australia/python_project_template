import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u

from my_package.load_data import PULSAR_CSV_PATH

def input_data(csv_path=PULSAR_CSV_PATH):
    """Reads the CSV file and returns a DataFrame with the RA and Dec converted to degrees.

    Parameters
    ----------
    csv_path : str
        Path to the CSV file containing the pulsar data.
        If none provided will use the pulsar data included with the package.

    Returns
    -------
    df : pandas.DataFrame
        Pandas DataFrame containing the pulsar data with RA and Dec in degrees.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv('my_package/data/pulsars.csv')

    # Add new columns to df
    df['RA (deg)']  = 0
    df['Dec (deg)'] = 0

    # Loop over dataframe and convert RA and Dec to degrees
    for index, row in df.iterrows():
        ra_hms  = row['RA (HMS)']
        dec_hms = row['Dec (DMS)']

        # Create a SkyCoord object and specify the units
        c = SkyCoord(ra=ra_hms, dec=dec_hms, unit=(u.hourangle, u.deg))
        # Access the converted RA and Dec in degrees
        ra_deg  = c.ra.deg
        dec_deg = c.dec.deg

        # Update the DataFrame with the converted values
        df.at[index, 'RA (deg)']  = ra_deg
        df.at[index, 'Dec (deg)'] = dec_deg

    return df


def filter_by_name(df, source_names):
    """Filters the DataFrame by source name.

    Parameters
    ----------
    df : pandas.DataFrame
        Pandas DataFrame containing the pulsar data with RA and Dec in degrees.
    source_names : list of str
        A list of source names to filter the DataFrame by.

    Returns
    -------
    df : pandas.DataFrame
        Pandas DataFrame containing the pulsar data with RA and Dec in degrees.
        Filtered by source name.
    """
    # Filter the DataFrame by source
    df = df[df['Source Name'].isin(source_names)]
    return df


def filter_by_declination(df, min_dec=-90, max_dec=90):
    """Filters the DataFrame by declination.

    Parameters
    ----------
    df : pandas.DataFrame
        Pandas DataFrame containing the pulsar data with RA and Dec in degrees.
    min_dec : float
        Minimum declination to filter by.
    max_dec : float
        Maximum declination to filter by.

    Returns
    -------
    df : pandas.DataFrame
        Pandas DataFrame containing the pulsar data with RA and Dec in degrees.
        Filtered by declination.
    """
    # Filter the DataFrame by declination
    df = df[(df['Dec (deg)'] > min_dec) & (df['Dec (deg)'] < max_dec)]
    return df