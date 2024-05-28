import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('querry.csv')

# Convert the time column to datetime format
df['time'] = pd.to_datetime(df['time'])

# Extract the magnitudes
magnitudes = df['mag']

# Calculate the seismic moment for each earthquake
# seismic_moment = 10**(1.5 * magnitudes + 9.1)
seismic_moment = 10**(1.5 * magnitudes + 16.05)
#(Kanamori and Hanks, 1979)

# Add the seismic moment to the DataFrame
df['seismic_moment'] = seismic_moment

# Sort the DataFrame by time
df = df.sort_values('time')

# Calculate the cumulative seismic moment
df['cumulative_seismic_moment'] = df['seismic_moment'].cumsum()

# Plot the cumulative seismic moment release over time
plt.figure(figsize=(10, 6))
plt.plot(df['time'], df['cumulative_seismic_moment'], marker='o', linestyle='-', markersize=2)
plt.xlabel('Time')
plt.ylabel('Cumulative Seismic Moment (Nm)')
plt.title('Cumulative Seismic Moment Release Over Time')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.show()