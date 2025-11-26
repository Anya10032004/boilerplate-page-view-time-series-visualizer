import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df = df.set_index('date')

# Clean data

ds_sorted = df.sort_values(by='value')
cutoff_1 = ds_sorted.quantile(0.025)
cutoff_2 = ds_sorted.quantile(0.975)
df = df[(df['value'] < cutoff_2['value'])
                       | (df['value'] <= cutoff_1['value'])
                      ]
df['date'] = pd.to_datetime(df.index)

def draw_line_plot():
        dates = pd.date_range(start = '2016-07', end = '2020-01', freq = '6MS')
        fig = plt.figure(figsize=(18, 6)) 
        plt.plot(df['date'], df['value'], color = 'red') 
        plt.xticks(dates, rotation = 0) 
        plt.ylim(2000, 180000)
        plt.yticks(range(20000, 180001, 20000)) 
        plt.xlabel("Date") 
        plt.ylabel("Page Views")
        plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019") 
        plt.subplots_adjust(left=0.08, right=0.98, top=1, bottom=1)
        plt.tight_layout() 
        plt.show() 



        # Save image and return fig (don't change this part)
        fig.savefig('line_plot.png')
        return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





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

    # for each year:
    





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
