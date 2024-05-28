import pandas as pd
import pygmt

# Load the CSV file into a DataFrame
df = pd.read_csv('querry.csv')

# Calculate the region (min and max lat/lon with 1 degree padding)
min_lat = df['latitude'].min() - 1
max_lat = df['latitude'].max() + 1
min_lon = df['longitude'].min() - 1
max_lon = df['longitude'].max() + 1

# Adjust the longitude range to be within [-180, 180]
if min_lon < -180:
    min_lon = -180

if max_lon > 180:
    max_lon = 180

# Create a PyGMT figure

fig = pygmt.Figure()
fig.basemap(
    region=[min_lon, max_lon, min_lat, max_lat],
    projection="M6i",
    frame=["xa45fg", "ya45fg", "WSrt"],
)

# fig = pygmt.Figure()

# Create a map with coastlines using the calculated region
# fig.basemap(region=[min_lon, max_lon, min_lat, max_lat], projection="M6i", frame=True)

# Plot the earthquake data
# fig.plot( x=df['longitude'],  y=df['latitude'],  size=df['mag'] * 0.1, style="cc", fill="red3",  pen="black", transparency=50)

x=df['longitude']
y=df['latitude']
m=df['mag'] * 0.03

fig.coast(shorelines=True, land="#666666", water="skyblue")
# plot seems to need to come first
fig.plot(
    x=x,
    y=y,
    style="c",
    size=m,
    fill="red3",
)


# Add a color bar for magnitude
# fig.colorbar(frame='af+l"Earthquake Magnitude"')

# Add a title
fig.text(text="Earthquake Locations and Magnitudes", position="TL", font="18p,Helvetica-Bold,black")

# Show the plot
fig.show()