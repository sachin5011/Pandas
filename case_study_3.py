import pandas as pd
# Library for data visualization
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


"""
=> Key Learnings : 
 01. How to fetch random sample from the dataset?
 02. isin
 03. between
 04. unique
 05. dropna
 06. replace
 07. duplicate
 08. drop_duplicate
 09. astype
 10. apply
 11. What is univariate analysis?
 12. What is bivariate analysis?
 13. Memory Optimization.
"""

pd.set_option("display.max_column", None)

data = pd.read_csv(".\case_study_datasets\\adult_income.csv")
# print(data)
# print(data.columns)


# ===== Display top 10 rows of dataset
# print(data.head(10))

# ==== Display last 10 rows of dataset
# print(data.tail(10))

# ==== Find the shape of the dataset(Number of rows and column)
# print(data.shape)
# print("Number of rows : ",data.shape[0])
# print("Number of column : ",data.shape[1])

# ==== Getting the information of the dataset for examaple number of rows and column, datatypes, memory etc.
# print(data.info())

# ==== Fetch randon sample from dataset (50%)
# data1 = data.sample(frac=0.50, random_state=100)
# print(data1)

# ==== check the null values in dataset
# ====>  NOTE : axis=1 for column,   axis=0 for row
# print(data.isnull().sum())

# print(sns.heatmap(data.isnull()))

# ==== Perform the data cleansing and replace ? with nan
# print(data[data.isin(["?"])].count())
data['workclass'] = data['workclass'].replace('?', np.nan)
data['occupation'] = data['occupation'].replace('?', np.nan)
data['native-country'] = data['native-country'].replace('?', np.nan)
# print(data[data.isin(["?"])].count())
# print(data.isnull().sum())
# print(sns.heatmap(data.isnull()))


# ==== Drop all missing values
# Note : Before dropping check the % of missing values
percent_missing = (data.isnull().sum()*100)/len(data)
# print(percent_missing)
# dropping the na value rows
data.dropna(how='any', inplace=True)
# print(data.shape)

# === Check Duplicate data and drop them
duplicate_data = data.duplicated().any()
# print(duplicate_data) # showing true means some duplicates data is present in dataset
data = data.drop_duplicates()
# print(data.shape)

# ==== Get all the statistics about the datasetr
# print(data.describe(include="all"))


# ==== Drop the columns education-num, captial-gain and capital-loss
# print(data.columns)
# data.drop(['educational-num', 'capital-gain', 'capital-loss'], axis=1, inplace=True)
# print(data.columns)

# ++++++=========== UNIVARIATE ANALYSIS ============++++++
# ===== What is the distribution of age column?
# print(data.columns)
# print(data["age"].describe())
# print(data['age'].hist())
# data['age'].hist()
# print(plt.hist(data['age']))

# ===== Find total number of Persons having age between 17 to 48(inclusive ) using between method
# print(data[data['age'].between(17,48)].count())
# print(data[(data['age']>=17) & (data['age']<=48)].count())
# print(sum(data['age'].between(17,48)))
# print(sum((data['age']>=17) & (data['age']<=48)))

# ===== What is the distribution of workclass column?
# print(data.columns)
# print(data['workclass'].describe(include='all'))

# ==== How many persons having bachelors ans masters degree?
# print(data.columns)
bachelor_filter = data['education'] == "Bachelors"
master_filter = data['education'] == 'Masters'
# print(len(data[bachelor_filter | master_filter]))

# OR
# print(sum(data['education'].isin(['Bachelors', 'Masters'])))


# +++++++============ BIVARIATE ANALYSYS =============+++++++++
# print(data.columns)
sns.boxplot(x='income', y='age', data=data)
# plt.show()

# ==== Replace salary <=50k , >=50k to 0,1
# print(data.columns)
# print(data['income'].value_counts())

def changesalary(income):
    if income == "<=50K":
        return 0
    else:
        return 1

# data["new_salary"] = data['income'].apply(changesalary)
# print(data.head())

# OR
# data['income'].replace(to_replace=["<=50K", ">50K"], value=[0,1], inplace=True)
# print(data.head())

# ===== Which workclass getting highest salary
# print(data.columns)
# print(data.info())
# print(data.groupby('workclass')['income'].mean())

# ==== Who has better chance to get higher salary Male or Female
# print(data.columns)
# print(data.groupby('gender')['income'].mean())


# ==== Convert workclass column datatype to Category datatype
# print(data.info())
# data['workclass'] = data['workclass'].astype("category")
# print(data.info())


