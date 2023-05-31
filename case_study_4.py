import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_column', None)
data = pd.read_csv(".\case_study_datasets\\titanic.csv")

# print(data.info())

# ==== Get the first 10 rows from dataset
# print(data.head(10))

# ==== get the last 10 rows from the dataset
# print(data.tail(10))

# ==== get the shape of the dataset
# print(data.shape)
# print("Number of rows : ", data.shape[0])
# print("Number of columns : ", data.shape[1])

# ==== Get the information about our dataset total number of rows, total number of columns, datatype and memory
# print(data.info())

# ==== Get overall statics about dataset
# print(data.describe(include='all'))


# ======= DATA FILTERING
# print(data['Name'])

# ----> filtering all names who are female
# print(data.columns)
# print(data[data['Sex']=='female']['Name'])

# -----> Getting the number of people survived
# print(data.columns)
# print(data[data['Survived'] == 1]['Survived'].count())

# ==== Getting the null values in dataset
# print(data.isnull().sum())

#  --> plotting graph
# sns.heatmap(data.isnull())
# plt.show()

# --> percentage missing
# per_missing = (data.isnull().sum() * 100)/len(data)
# print(per_missing)

# DROP COLUMN
# data.drop(["Embarked", "Sex"], axis=1, inplace=True)
# print(data.columns)


# ===== Handling Missing Values
# print(data.columns)
# print(data["Embarked"].mode()) # s is most frequent value in this column
# data['Embarked'].fillna('S', inplace=True) # all misiing values is going to filled with s
# print(data.isnull().sum())

# ==== Filling the missing value of age column with mean value of age
# print(data.isnull().sum())
# print(data['Age'].fillna(data['Age'].mean(), inplace=True))
# # we will get missing value count for age column = 0
# print(data.isnull().sum())

# ========= Categorical Data Encoding
# getting the unique values in a spefic column
# print(data['Sex'].unique())
# x =data['Sex'].map({"male":1, "female":0})
# print(data.head())
# inserting the data at spefic index
# data.insert(index, Column_name, value)
# data.insert(5, 'Gender', x)
# print(data.head())

# print(data['Embarked'].unique())
# data_to_encode = data["Embarked"].map({'S':1, "c":2, "Q":3, "nan":0})
# data.insert(12, "Embarked_new", data_to_encode)
# print(data.head())

# print(pd.get_dummies(data, columns=['Embarked']))
# print(data.head())


# ======= Univariate Analysis
# 1. how many people survived and how many died?
# print(data['Survived'].value_counts())
import seaborn as sns
import matplotlib.pyplot as plt

# sns.countplot(data['Survived'])
# plt.show()

# 2. How many Passengers were in first class, second class and third class?
# print(data.columns)
# print(data['Pclass'].value_counts())
# sns.countplot(data['Pclass'])
# plt.show()

# 3. Number of male and female passengers?
# print(data.columns)
# print(data['Sex'].value_counts())
# sns.countplot(data['Sex'])
# plt.show()

plt.hist(data['Age'])
# plt.show()

# =====  Bivariate Analysis
# 1. Who has better chance of survival male or female
sns.barplot(x = "Sex", y="Survived", data=data)
# plt.show()

# 2. Which passenger class have better chance of survival(First, Second or Third)
sns.barplot(x="Pclass", y='Survived', data=data)
# plt.show()

# =========++++++ Feature Engineering ++++++++++===========
print(data.columns)
# getting the family size by sibsp and parch column
data['Family_size'] = data['SibSp']+data['Parch']
# print(data['Family_size'])

# Find fare per person
data["Fare_per_person"]= (data['Fare']/ data["Family_size"]+1)
print(data["Fare_per_person"])