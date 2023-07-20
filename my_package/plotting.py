import matplotlib.pyplot as plt
from numpy import radians


def molleweide_plot(df):
    """Plots the pulsars in a Molleweide projection and saves as a png called pulsar_plot.png.

    Parameters
    ----------
    df : pandas.DataFrame
        Pandas DataFrame containing the pulsar data with RA and Dec in degrees.
    """
    # Plot the pulsars
    fig = plt.figure(figsize=(6, 4))
    # Molleweide projection gives us a nice view of the whole sky
    ax = plt.axes(projection='mollweide')
    plt.grid(True, color='gray', lw=0.5, linestyle='dotted')
    ax.set_xticklabels(['22h', '20h', '18h', '16h', '14h','12h','10h', '8h', '6h', '4h', '2h'])

    # Convert RA and Dec to radians and plot
    ax.scatter(radians(-df['RA (deg)'] + 180), radians(df['Dec (deg)']), s=0.2)
    plt.savefig("pulsar_plot.png", dpi=300, bbox_inches='tight')