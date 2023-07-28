import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Use Pandas to import the data from epa-sea-level.csv
sea_df = pd.read_csv('./epa-sea-level.csv')
print(sea_df)

# data analysis

sea_df.info()
print(sea_df.shape)
print(sea_df.columns)
print(sea_df.describe())

print(sea_df.isnull().sum())

print(sea_df['NOAA Adjusted Sea Level'])



# Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
plt.figure( figsize=(12,6))
plt.scatter(x= sea_df.Year, y= sea_df['CSIRO Adjusted Sea Level'])
plt.title('CSIRO on Sea Level')
plt.xlabel('Year')
plt.ylabel('CSIRO Adjusted Sea Level')

# Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.

# first line of best fit
reg = linregress(sea_df['Year'], sea_df['CSIRO Adjusted Sea Level'])
pred_Ax = np.arange(sea_df['Year'].min(), 2050,1)
pred_Ay = pred_Ax*reg.slope + reg.intercept 
plt.plot(pred_Ax, pred_Ay, c='r')


# Create second line of best fit
sea_2000 = sea_df[sea_df['Year'] >= 2000]

reg_b = linregress(sea_2000['Year'], sea_2000['CSIRO Adjusted Sea Level'])
pred_Bx = np.arange(2000, 2050, 1)
pred_By = pred_Bx*reg_b.slope + reg_b.intercept
plt.plot(pred_Bx, pred_By, c='green')

# Add labels and title
plt.title('Rise in Ocean Level')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')






