import pandas as pd

demographic_data = pd.read_csv('adult.data.csv')
print(demographic_data)

# How many of each race are represented in this dataset?
race_count = demographic_data['race'].value_counts()
print(race_count)

# What is the average age of men?
#average_age_men = demographic_data[demographic_data['sex'] == 'Male', 'age'].mean()
#print(average_age_men)

p= demographic_data[demographic_data['sex']== 'Male']
print(p)
average_age_mean = p['age'].mean()
print(average_age_mean)

# What is the percentage of people who have a Bachelor's degree?
education_data = demographic_data.groupby('education')[['education-num']].count()
print(education_data)
education_data['percentage'] = (education_data/ education_data.sum())*100
#percentage = (education_data['Bacherlors']/ education_data.sum())* 100
print(education_data)

#print(education_data.index)

percentage_bachelors  = education_data.loc['Bachelors' ,'percentage']
print(percentage_bachelors )

# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

edu_salary = demographic_data[['education', 'salary']]
print(edu_salary)

edu_salary.set_index('education', inplace = True)
print(edu_salary)

higher_education = edu_salary.loc[['Bachelors', 'Masters',  'Doctorate']]
print(higher_education)


#print(edu_salary.sort_index())
#print(edu_salary != edu_salary.index['Bachelors', 'Masters',  'Doctorate'])

lower_education = edu_salary.loc[['HS-grad', '9th', '10th', 'Assoc-voc', 'Some-college']]
print(lower_education)

# percentage with salary >50K

high_education_rich =  higher_education.loc[higher_education['salary'] == ">50K"]
#print(high_education_rich)

high_edu_rich = high_education_rich.groupby(high_education_rich.index)[['salary']].count()
#print(high_edu_rich)

#h_edu_rich = high_edu_rich.rename(columns= {'salary' : 'num_salary_>50k'})
#print(high_edu_rich)

total_salary_hight_education = high_edu_rich['salary'].sum()
#print(total_salary_hight_education)

high_edu_rich['percentage'] = (high_edu_rich['salary'] / total_salary_hight_education) * 100
#print(h_edu_rich)

highter_education_rich = high_edu_rich['percentage']
print(highter_education_rich)



print('*******************************')
#***********************************

low_education_rich = lower_education.loc[lower_education['salary'] == ">50K"]
#print(low_education_rich)

low_edu_rich = low_education_rich.groupby(low_education_rich.index)[['salary']].count()
#print(low_edu_rich)

#l_edu_rich = low_edu_rich.rename(columns= {'salary' : 'num_salary_>50k'})
#print(l_edu_rich)

total_salary_low_education = low_edu_rich['salary'].sum()
#print(total_salary_low_education)

low_edu_rich['percentage']= (low_edu_rich['salary'] / total_salary_low_education) * 100
#print(l_edu_rich)

lower_education_rich = low_edu_rich['percentage']

print(lower_education_rich)


# What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = demographic_data["hours-per-week"].min ()
print(min_work_hours)

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?

num_min_workers= demographic_data[demographic_data['hours-per-week'] == min_work_hours]
print(num_min_workers)

rich_percentage = num_min_workers.loc[num_min_workers['salary'] == ">50K"].size / num_min_workers.size * 100
print(rich_percentage)

 # What country has the highest percentage of people that earn >50K?

countries_demographic_salary = demographic_data[['native-country','salary']]
print(countries_demographic_salary)

countries_high_earning = countries_demographic_salary[countries_demographic_salary['salary'] == ">50K"]


h_eraning_country = countries_high_earning.groupby('native-country')[['salary']].count()
print(h_eraning_country)

##max_salary = h_eraning_country.max()
#print(max_salary)

highest_eraning_country =  h_eraning_country /  countries_high_earning.size * 100
#print(highest_eraning_country)

highest_earning_country_percentage = highest_eraning_country.max()
print(highest_earning_country_percentage)

 # Identify the most popular occupation for those who earn >50K in India.

print(demographic_data.columns)

demographic_dat_india = demographic_data.loc[demographic_data['native-country'] == 'India']
print(demographic_dat_india)
high_incom_india = demographic_dat_india.loc[demographic_dat_india['salary'] == ">50K"]
print(high_incom_india)

ocupation_dat_india = high_incom_india['occupation'].value_counts()
print(ocupation_dat_india )

top_IN_occupation = ocupation_dat_india.idxmax()

print('the most popular ocupation in India is:',top_IN_occupation)






#highest_earning_country_percentage = 

 #highest_earning_country = demographic_data[demographic_data['salary'] == ">50K" ].max()
 #print(higest_erning_country)









