import pandas as pd


#calculate_demographic_data = pd.read_csv('adult.data.csv')
#print(calculate_demographic_data)

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("./adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'men'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    education_data = df.groupby('education')[['education- num']].count() 

    education_data['percentage'] =(education_data/education_data.sum())*100
  
    percentage_bachelors = education_data.loc['Bachelors','percentage']

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    edu_salary = df[['education', 'salary']]
    edu_salary.set_index('education', inplace = True)
    
    higher_education = edu_salary.loc[['Bachelors', 'Masters',
    'Doctorate']]
    lower_education = edu_salary.loc[['HS-grad','9th','10th','Assoc-voc','Some- college']]
  
    # percentage with salary >50K
    high_education_rich = higher_education.loc[higher_education['salary'] == ">50K"]
    high_edu_rich = high_education_rich.groupby(high_education_rich.index) [['salary']].count()
    total_salary_hight_education = high_edu_rich['salary'].sum()
    high_edu_rich['percentage'] = (high_edu_rich['salary'] / 
 total_salary_hight_education) * 100
    higher_education_rich = high_edu_rich['percentage']

    low_education_rich = lower_education.loc[lower_education['salary'] == ">50K"]
    low_edu_rich = low_education_rich.groupby(low_education_rich.index) [['salary']].count()
    total_salary_low_education = low_edu_rich['salary'].sum()
    low_edu_rich['percentage']= (low_edu_rich['salary'] /
total_salary_low_education) * 100
    lower_education_rich = low_edu_rich['percentage']

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    
  
    min_work_hours = df["hours-per-week"].min ()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage =  num_min_workers.loc[num_min_workers['salary'] ==  ">50K"].size / num_min_workers.size * 100

    # What country has the highest percentage of people that earn >50K?
    countries_demographic_salary = df[['native- country','salary']]
    countries_high_earning=countries_demographic_salary[countries_demographic_salary['salary'] == ">50K"]
    h_eraning_country = countries_high_earning.groupby('native-country')[['salary']].count()
    
    highest_earning_country = h_eraning_country / countries_high_earning.size * 100
  
    highest_earning_country_percentage = highest_earning_country.max()

    # Identify the most popular occupation for those who earn >50K in India.
    demographic_dat_india = df.loc[df['native-country'] == 'India']
    high_incom_india= demographic_dat_india.loc[demographic_dat_india['salary'] == ">50K"]
    ocupation_dat_india = high_incom_india['occupation'].value_counts()
    top_IN_occupation = ocupation_dat_india.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
