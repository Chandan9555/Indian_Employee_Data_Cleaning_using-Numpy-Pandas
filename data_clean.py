# importing necessary libraries
import pandas as pd
import numpy as np

# laoding dataset
df = pd.read_csv('indian_employee_dataset.csv')
print(df.head())

# checking the missing values
print('Missing values in each column')
print(df.isnull().sum())

df['Salary (INR)'] = df['Salary (INR)'].fillna(df['Salary (INR)'].mean(), inplace=True)

df['Performance Rating'] = df['Performance Rating'].fillna(df['Performance Rating'].median(), inplace=True)

df = df.replace([np.inf, -np.inf], np.nan, inplace= True)
df = df.fillna(df.mean(numeric_only=True))

# remove duplicate records
df.drop_duplicates(inplace=True)

# replace negative salaries
df['Salary (INR)'] = np.where(df['Salary (INR)']<0, df['Salary (INR)'].mean(), df['Salary (INR)'])

salary_mean = df['Salary (INR)'].mean()
salary_std = df['Salary (INR)'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

# remove rows where salary is too high or too low 
df = df[(df['Salary (INR)'] >= lower_bound) & (df['Salary (INR)'] <= upper_bound)]

df.to_csv('cleaned_indian_employee_Data.csv', index= False)
print('Data cleaning completed! Saved as "cleaned_indian_employee_Data.csv"')
