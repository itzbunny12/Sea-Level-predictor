import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')

    # Create first line of best fit (1880–2050)
    res_full = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_full = pd.Series(range(1880, 2051))
    y_full = res_full.intercept + res_full.slope * x_full
    plt.plot(x_full, y_full, 'r', label='Best Fit: All Data')

    # Create second line of best fit (2000–2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = res_recent.intercept + res_recent.slope * x_recent
    plt.plot(x_recent, y_recent, 'green', label='Best Fit: From 2000')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
