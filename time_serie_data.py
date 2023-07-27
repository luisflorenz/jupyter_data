import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df_time = pd.read_csv('./fcc-forum-pageviews.csv', index_col='date')
print(df_time)

print(df_time.columns)
df_time.info()

print(df_time.describe())

# Clean data
#percentage_time = df_time.value/1000
#print(percentage_time)
#df_time.value = percentage_time
#print(df_time)

#print(df_time.mean())
df_time =  df_time.loc[(df_time['value'] > df_time['value'].quantile(0.025)) & (df_time['value'] < df_time['value'].quantile(0.975))]
print(df_time)


#Create a draw_line_plot function that uses Matplotlib to draw a line chart. The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.
#date= range(2016-2019)
df_time.index =pd.to_datetime(df_time.index)
plt.figure(figsize=(12, 6))
plt.plot(df_time.index,df_time.value, color='red',linewidth=0.8)
plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
plt.xlabel('Date')
plt.ylabel('Page Views')



# Draw bar plot, It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.
df_bar = df_time.copy()
df_bar['Year'] = pd.DatetimeIndex(df_bar.index).year
df_bar['Month'] = pd.DatetimeIndex(df_bar.index).month_name()
df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean()
print(df_bar)

fig = df_bar.plot(kind= 'bar', figsize = (15,10)).figure

plt.title('')
plt.xlabel('Years')
plt.ylabel('Average Page Views')
lg = plt.legend(title= 'Months', fontsize = 15, labels = 'month_names')
title = lg.get_title()
title.set_fontsize(15)

# Create a draw_box_plot function that uses Searborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be "Year-wise Box Plot (Trend)" and the title of the second chart should be "Month-wise Box Plot (Seasonality)". Make sure the month labels on bottom start at "Jan" and the x and x axis are labeled correctly.

 # Yearly boxplot
df_box = df_time.copy()
df_box['Year'] = pd.DatetimeIndex(df_box.index).year
df_box['Month'] = pd.DatetimeIndex(df_box.index).month_name()
plt1 =sns.boxplot(x = "Year", y = "value", data = df_box)
plt1.set_title("Year-wise Box Plot (Trend)")
plt1.set_xlabel('Year')
plt1.set_ylabel('Page Views')

# Monthly boxplot
plt2=sns.boxplot(x='Month',y='value',data=df_box)
plt2.set_title("Month-wise Box Plot (Trend)")
plt2.set_xlabel('Month')
plt2.set_ylabel('Page Views')


#print(df_box)



#print(df_time.value.first_valid_index())



#df_time = df_time[[['date
# '], ['value']/100]]
#print(df_time)