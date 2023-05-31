import pandas as pd
import numpy as np
# this line will show all the column from dataset
pd.set_option('display.max_column', None)

data = pd.read_csv(".\case_study_datasets\Salaries.csv")
# print(data.columns)
# print(data.info())
# print(data.head())


# ==== Display top 10 rows of dataset
# print(data.head(10))

# ==== Check last 10 rows of dataset
# print(data.tail(10))

# ==== Find the shape of our dataset (number of rows and column)
# print(data.shape)
# print("Total number of rows : ",data.shape[0])
# print("Total number of columns : ",data.shape[1])


# ==== Getting information of dataset ie number of rows and column datatype and memory
# print(data.info())

# ==== Check null values in dataset
# print(data.isnull().sum())

# === Drop column Id, Notes, Agency and Status
# ====>  NOTE : axis=1 for column,   axis=0 for row
# drop_data = data.drop(['Id', 'Notes', 'Agency', 'Status'], axis=1)
# print(drop_data.columns)

# === Get all the statistics about dataset
# print(data.describe(include='all'))

# === Find the occurance of top 5 employee names
# print(data["EmployeeName"].value_counts().head(5))

# === Find the number of unique job title
# print(data.columns)
# print(data["JobTitle"].nunique()) # nununioque() gives count

# === Total number of job title contain Captain
# print(data.columns)
# print(len(data[data['JobTitle'].str.contains("Captain", case=False)]))
# OR
# print(data[data['JobTitle'].str.contains("Captain", case=False)].count())


# === Display all employee name from fire department
# print(data.columns)
# print(data[data["JobTitle"].str.contains("fire department", case=False)]["EmployeeName"])

# === Display Maximun, Minimun and average BasePay
# print(data.columns)
# print("Maximum Base Pay : ",data["BasePay"].max())
# print("Minimum Base Pay : ",data["BasePay"].min())
# print("Average Base Pay : ",data["BasePay"].mean())


# === Replace Not Provided in Employee name column to NAN
# data['EmployeeName'] = data['EmployeeName'].replace('Not provided', np.nan)
# print(data['EmployeeName'])

# === Drop the rows having more than 5 missing values
# ====> NOTE : to make the drop permanent we have to use inplace=True
# print(data.count())
# print(data.drop(data[data.isnull().sum(axis=1)>5].index, axis=0, inplace=True))


# === Find job title for Albert Pardini
# print(data[data["EmployeeName"] == "Albert Pardini"]['JobTitle'])

# === How much Albert Pardini Makes including Benifits
# print(data.columns)
# print(data[data["EmployeeName"] == "Albert Pardini"]['TotalPayBenefits'])


# ===  Display the name of the person having Maximum basepay
# print(data.columns)
# print(data[data["BasePay"] == data["BasePay"].max()]['EmployeeName'])

# === Find average basepay for all employee per year
# print(data.columns)
# print(data.info())
# print((data.groupby('Year'))["BasePay"].mean())

# === Find the average basepay of all the employees per jobtitle
# print(data.columns)
# print(data.groupby("JobTitle")['BasePay'].mean())


# === Find the average basepay of employee having jobtitle ACCOUNTANT
# print(data.columns)
# print(data[data['JobTitle'] == "ACCOUNTANT"]['BasePay'].mean())


# === Find top 5 common jobs
# print(data["JobTitle"].value_counts().head())
