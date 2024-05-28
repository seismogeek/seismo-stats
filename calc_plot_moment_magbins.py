import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('querry.csv')

# Extract the magnitudes
magnitudes = df['mag']

# Calculate the seismic moment for each earthquake
# seismic_moment = 10**(1.5 * magnitudes + 9.1)
seismic_moment = 10**(1.5 * magnitudes + 16.05)
#(Kanamori and Hanks, 1979)

# Define the bins with size 1
bins = range(int(magnitudes.min()), int(magnitudes.max()) + 2)  # +2 to include the last bin edge

# Compute the histogram for the total seismic moment in each bin
total_moment_per_bin = np.zeros(len(bins) - 1)
for i in range(len(bins) - 1):
    in_bin = (magnitudes >= bins[i]) & (magnitudes < bins[i + 1])
    total_moment_per_bin[i] = seismic_moment[in_bin].sum()

# Print the total seismic moment for each bin
for i in range(len(total_moment_per_bin)):
    print(f"Magnitude {bins[i]} - {bins[i+1]}: {total_moment_per_bin[i]:.2e} Nm")

# Plot the total seismic moment released in each magnitude bin
plt.figure(figsize=(10, 6))
plt.bar(bins[:-1], total_moment_per_bin, width=1, edgecolor='black', align='edge', alpha=0.7)
plt.xlabel('Magnitude')
plt.ylabel('Total Seismic Moment (Nm)')
plt.title('Total Seismic Moment Released in Each Magnitude Bin')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xticks(bins)  # Set x-ticks to bin edges

# Show the plot
plt.show()
