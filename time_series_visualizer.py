import matplotlib.pyplot as plt
import pandas as pd
# import seaborn as sns
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
        plt.subplots_adjust(left=0.08, right=0.98, top=0.9, bottom=0.1)
        plt.tight_layout() 
        plt.show() 



        # Save image and return fig (don't change this part)
        fig.savefig('line_plot.png')
        return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['year'] = df['date'].dt.year
    df['month'] =  df['date'].dt.month
    df_bar =  df[['value', 'year', 'month']]

    # Draw bar plot
    for_graph_pivot = df_bar.pivot_table(
         index = "month",
         columns = "year",
         values = "value",
         aggfunc = "mean"
    )
    transpose_data = for_graph_pivot.transpose()

    month =  ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September', 'October', 'November', 'Desember']
    transpose_data.columns = month

    fig = plt.figure(figsize=(8, 7))
    transpose_data.plot(kind = "bar", width = 0.5)
    plt.title("Average page views each month")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.xticks(rotation = 0)
    plt.legend(title = "Month")
    plt.tight_layout()
    plt.show()





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
    year = [2016, 2017, 2018, 2019]
    years = {}
    ii = 0
    ava = []
    for a in year:
        if a not in  years:
              years[a] = []
        years[a] = df_box[df_box['year'] == a ]['value'].tolist()
    
    dataa = []
    for_x_axis_two = []
    for_x_axis_one = []
    num = 1
    for a,b in years.items():
        dataa.append(b)
        for_x_axis_two.append(a)
        for_x_axis_one.append(num)
        num += 1
    
    # for each month:
    month = list(range(1, 13))
    months = {}
    ava = []
    for a in month:
         if a not in  months:
              months[a] = []
         months[a] = df_box[df_box['month'] == a]['value'].tolist()
    

    dataa_m = []
    for_x_axis_two_m = []
    for_x_axis_one_m = []
    num = 1
    for a,b in months.items():
        dataa_m.append(b)
        for_x_axis_two_m.append(a)
        for_x_axis_one_m.append(num)
        num += 1

    # memploting untuk menunjukan 
    fig = plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.boxplot(dataa)
    plt.xticks(for_x_axis_one, for_x_axis_two)
    plt.ylim(0, 180000)
    plt.ylabel("Values")
    plt.title("Box Plot for Each year")

    plt.subplot(1, 2, 2)
    plt.boxplot(dataa_m)
    plt.xticks(for_x_axis_one_m, for_x_axis_two_m)
    plt.ylim(0, 200000)
    plt.ylabel("Values")
    plt.title("Box Plot for Each month")

    
    plt.show()




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
