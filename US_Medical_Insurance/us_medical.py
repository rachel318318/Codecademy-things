# US Medical Insurance Costs project
# Starting on May 1st, 2021
# Rachel Lee

import pandas as pd

df = pd.read_csv('insurance.csv')

print(df.head())

age = df['age']
sex = df['sex']
bmi = df['bmi']
child = df['children']
is_smoker = df['smoker']
region = df['region']
charges = df['charges']

print(age.mean())
num_female = sex[sex == 'female'].count()
num_male = sex[sex == 'male'].count()

female_percent = num_female/(num_male + num_female)
male_percent = num_male/(num_male + num_female)

print("asdf"[-2:])