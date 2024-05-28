
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('querry.csv')

# Convert the time column to datetime format
df['time'] = pd.to_datetime(df['time'])

# Define the size of the circles based on magnitude
size = df['mag'] * 10  # Adjust the scaling factor as needed

# Plot the earthquakes as circles in a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['time'], df['depth'], s=size, c=df['mag'], cmap='plasma', alpha=0.5)
plt.xlabel('Time')
plt.ylabel('Depth')
plt.title('Earthquakes Scatter Plot')
plt.colorbar(label='Magnitude')
plt.grid(True)
plt.show()