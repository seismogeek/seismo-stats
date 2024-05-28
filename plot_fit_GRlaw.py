import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('querry.csv')

# Extract the magnitudes
magnitudes = df['mag']

# Create a list of unique magnitudes sorted in ascending order
unique_magnitudes = np.sort(magnitudes.unique())

# Calculate the cumulative frequency for each unique magnitude
cumulative_freq = np.array([len(magnitudes[magnitudes >= mag]) for mag in unique_magnitudes])

# Log-transform the cumulative frequency
log_cumulative_freq = np.log10(cumulative_freq)

# Perform linear regression using numpy
A = np.vstack([unique_magnitudes, np.ones_like(unique_magnitudes)]).T
m, c = np.linalg.lstsq(A, log_cumulative_freq, rcond=None)[0]

# The slope is -b and the intercept is a in the Gutenberg-Richter law
b = -m
a = c

# Print the best-fit values for a and b
print(f"Best-fit values:\na = {a}\nb = {b}")

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(unique_magnitudes, log_cumulative_freq, 'o', label='Data')
plt.plot(unique_magnitudes, m * unique_magnitudes + c, 'r-', label=f'Best-fit line: log10(N) = {c:.2f} - {abs(m):.2f}M')
plt.xlabel('Magnitude')
plt.ylabel('Log10(Cumulative Frequency)')
plt.title('Gutenberg-Richter Law')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()
