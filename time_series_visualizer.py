import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/refs/heads/main/fcc-forum-pageviews.csv")
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
# Clean data
low = df['value'].quantile(0.025)
high = df['value'].quantile(0.975)
df = df.loc[(df['value'] >= low) & (df['value'] <= high)]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], color='r', linewidth=1)

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df.loc[:, 'year'] = df.index.year
    df.loc[:, 'month'] = df.index.month_name()
    df_bar = df.groupby(['year', 'month'])['value'].mean().reset_index()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15, 8))
    months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
    sns.barplot(data=df_bar, x='month', y='value', hue='year', order=months, ax=ax)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    sns.boxplot(x='month', y='value', data=df_box, order=months, ax=ax2)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")

    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig