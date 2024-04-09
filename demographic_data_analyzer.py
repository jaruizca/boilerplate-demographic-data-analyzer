import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv",na_values="?")

    rich = df["salary"] == ">50K"

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = np.round(df[df.sex == "Male"]["age"].mean(),decimals=1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = np.round((df["education"] == "Bachelors").mean() * 100,decimals=1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = (df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate")
    lower_education = ~higher_education

    # percentage with salary >50K
    higher_education_rich = np.round((higher_education & rich).sum() / higher_education.sum() * 100, decimals=1)
    lower_education_rich  = np.round((lower_education & rich).sum() / lower_education.sum() * 100, decimals=1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()
    min_workers = df["hours-per-week"] == min_work_hours

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    counts = df[min_workers]["salary"].value_counts()
    rich_percentage = (counts/counts.sum())[">50K"]
    rich_percentage = np.round(rich_percentage * 100,decimals=1)

    # What country has the highest percentage of people that earn >50K?

    highest_earning = df.groupby("native-country")["salary"].apply(lambda x: (x==">50K").mean())
    highest_earning_country_percentage = np.round(highest_earning.max() * 100, decimals=1)
    highest_earning_country = highest_earning.idxmax()

    # Identify the most popular occupation for those who earn >50K in India.
    rich_indian = df[(df["native-country"] == "India") & rich]

    top_IN_occupation = rich_indian["occupation"].value_counts().idxmax()

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
