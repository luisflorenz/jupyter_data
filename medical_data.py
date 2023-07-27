import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

medical_df = pd.read_csv("./medical_examination.csv")

#print(medical_df)

medical_df.info()

print(medical_df.describe())

print(medical_df.columns)

print(medical_df.shape)

print(medical_df.isnull().sum())

# Add 'overweight' column
bmi_mass_index = medical_df.weight /(medical_df.height/100)**2
print(bmi_mass_index)

medical_df['overweight'] = (bmi_mass_index).apply(lambda x: 1 if x >25 else 0)
#overweight = (bmi_mass_index >25).astype(int)
#medical_df['overweight'] =  overweight
print(medical_df)

print(medical_df.overweight.unique())

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

medical_df['cholesterol'] = medical_df.cholesterol.apply(lambda x: 0 if x==1 else 1)
medical_df['gluc'] = medical_df.gluc.apply(lambda x: 0 if x==1 else 1)

print(medical_df)   

# Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight', The dataset should be split by 'Cardio' so there is one chart for each cardio value.

cardio_df = pd.melt(medical_df, value_vars=['cholesterol','gluc', 'smoke', 'alco', 'active', 'overweight'])
print(cardio_df)

# Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

cardio_df = pd.melt(medical_df, id_vars=['cardio'], value_vars=['cholesterol','gluc', 'smoke', 'alco', 'active', 'overweight'])
print(cardio_df)

# Draw the catplot with 'sns.catplot()'

cardio_figure = sns.catplot(cardio_df, x='variable', hue='value', col='cardio', kind='count')
cardio_figure.set_axis_labels('variable', '')
print(cardio_figure)

#Clean the data. Filter out the following patient segments that represent incorrect data:
# .diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
# .height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
# .height is more than the 97.5th percentile
# .weight is less than the 2.5th percentile
# .weight is more than the 97.5th percentile

cardio_heat = medical_df[(medical_df['ap_lo']<=medical_df['ap_hi'])&(medical_df['height']>=medical_df['height'].quantile(0.025)) & (medical_df['height']<=medical_df['height'].quantile(0.975))
          &(medical_df['weight']>=medical_df['weight'].quantile(0.025)) & (medical_df['weight']<=medical_df['weight'].quantile(0.975))]

# Calculate the correlation matrix
medical_corr_matrix = cardio_heat.corr()
print(medical_corr_matrix)

 # Generate a mask for the upper triangle

medical_corr_mask =  np.triu(medical_corr_matrix)
print(medical_corr_mask)

 # Set up the matplotlib figure

fig, ax = plt.subplots(figsize=(7, 5))


 # Draw the heatmap with 'sns.heatmap()'

#sns.heatmap(medical_corr_matrix, annot=True, fmt='.1f', linewidths=1, mask=medical_corr_mask, vmax='.8', center=0.09, square=True, cbar_kws={'shrink': 0.5})

sns.heatmap(
        medical_corr_matrix, annot=True, fmt='.1f', linewidths=1, mask=medical_corr_mask, 
        vmax=.8, center=0.09, square=True, cbar_kws={'shrink':0.5})

fig.savefig('heatmap.png')
#return fig
