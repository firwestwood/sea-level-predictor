import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Step 1: Import the data
df = pd.read_csv('epa-sea-level.csv')

# Step 2: Create Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', color='blue')

# Step 3: Perform Linear Regression on All Data
result_full = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
slope_full, intercept_full = result_full.slope, result_full.intercept
# Predict sea level through 2050
years_extended = pd.Series(range(1880, 2051))
plt.plot(years_extended, intercept_full + slope_full * years_extended, label='Best Fit Line (All Data)', color='green')

# Step 4: Perform Linear Regression on Data from 2000
df_recent = df[df['Year'] >= 2000]
result_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
slope_recent, intercept_recent = result_recent.slope, result_recent.intercept
# Predict sea level through 2050
years_recent = pd.Series(range(2000, 2051))
plt.plot(years_recent, intercept_recent + slope_recent * years_recent, label='Best Fit Line (2000+)', color='red')

# Step 5: Label the Plot
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Save and return the plot
plt.savefig('sea_level_plot.png')
plt.show()
