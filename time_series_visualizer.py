import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

# Load the dataset
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Data cleaning - Remove outliers (top and bottom 2.5%)
df_clean = df.copy()

# Remove values that are in the top 2.5% and bottom 2.5% of the data
percentile_2_5 = df_clean['value'].quantile(0.025)
percentile_97_5 = df_clean['value'].quantile(0.975)

df_clean = df_clean[(df_clean['value'] > percentile_2_5) & (df_clean['value'] < percentile_97_5)]

# Ensure proper data type conversion and prevent warnings
df_clean.loc[:, 'value'] = df_clean['value'].astype(float)

# Output the number of rows after cleaning
print(f"After cleaning, rows: {len(df_clean)}")

# Function to plot the line plot
def draw_line_plot():
    # Create a copy of the dataframe for plotting
    df_line = df_clean.copy()

    # Create a line plot
    plt.figure(figsize=(10, 5))
    plt.plot(df_line.index, df_line['value'], color='r')
    
    # Title and labels
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    
    # Save and show the plot
    plt.tight_layout()
    plt.savefig('line_plot.png')
    plt.show()

# Function to plot the bar plot
def draw_bar_plot():
    # Create a copy of the dataframe for plotting
    df_bar = df_clean.copy()

    # Group by year and month to calculate the average page views per month
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_monthly_avg = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Create a bar plot
    df_monthly_avg.plot(kind='bar', figsize=(12, 6))
    
    # Title and labels
    plt.title('Average Monthly Page Views (by Year)')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    
    # Add legend and show the plot
    plt.legend(title='Months', labels=[calendar.month_name[i] for i in range(1, 13)])
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    plt.show()

# Function to plot the box plot
def draw_box_plot():
    # Create a copy of the dataframe for plotting
    df_box = df_clean.copy()

    # Add year and month columns for boxplot analysis
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month

    # Create the boxplot for year-wise distribution
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_box)
    plt.title('Year-wise Box Plot (Trend)')

    # Create the boxplot for month-wise distribution
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df_box)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xticks(ticks=range(12), labels=[calendar.month_name[i] for i in range(1, 13)])

    # Show the plots
    plt.tight_layout()
    plt.savefig('box_plot.png')
    plt.show()

# Call the functions to create the plots
draw_line_plot()
draw_bar_plot()
draw_box_plot()









    