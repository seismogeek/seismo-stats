import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('querry.csv')

# Extract the magnitudes
magnitudes = df['mag']

# Define the bins with size 1
bins = range(int(magnitudes.min()), int(magnitudes.max()) + 2)  # +2 to include the last bin edge

# Compute the histogram
counts, bin_edges = np.histogram(magnitudes, bins=bins)

# Print the number of earthquakes in each bin
for i in range(len(counts)):
    print(f"Magnitude {bin_edges[i]} - {bin_edges[i+1]}: {counts[i]} earthquakes")

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.hist(magnitudes, bins=bins, edgecolor='black', alpha=0.7)
plt.xlabel('Magnitude')
plt.ylabel('Number of Earthquakes')
plt.title('Histogram of Earthquake Magnitudes')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xticks(bins)  # Set x-ticks to bin edges

# Show the plot
plt.show()
