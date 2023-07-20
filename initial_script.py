import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u
import matplotlib.pyplot as plt
from numpy import radians

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

# Print the DataFrame to check the degree calculation
print(df)

# Plot the pulsars
fig = plt.figure(figsize=(6, 4))
# Molleweide projection gives us a nice view of the whole sky
ax = plt.axes(projection='mollweide')
plt.grid(True, color='gray', lw=0.5, linestyle='dotted')
ax.set_xticklabels(['22h', '20h', '18h', '16h', '14h','12h','10h', '8h', '6h', '4h', '2h'])

# Convert RA and Dec to radians and plot
ax.scatter(radians(-df['RA (deg)'] + 180), radians(df['Dec (deg)']), s=0.2)
plt.savefig("pulsar_plot.png", dpi=300, bbox_inches='tight')


