import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_column", None)

# parsing the datetime column to date time from object using parse_dates
data = pd.read_csv(".\case_study_datasets\\udemy_courses.csv", parse_dates=["published_timestamp"])

# print(data.dtypes)
# ==== Display top 10 rows from dataset
# print(data.head(10))

# ==== Display last 10 rows from dataset
# print(data.tail(10))

# ==== find the shape of the dataset (number of rows and columns)
# print(data.shape)
# print("Number of rows : ",data.shape[0])
# print("Number of columns : ",data.shape[1])

# ===== Getting all the information about dataset like number of rows and column, datatype and memory used
# print(data.info())

# ==== Check null values in dataset
# if there is any missing valure it will print true else it will print False
# print(data.isnull().values.any())

# It will print the count of missing values column wise
# print(data.isnull().sum())

# Graph for null values
# sns.heatmap(data.isnull())
# plt.show()

# ==== Check for Duplicates and drop then
# checking duplicate values
dupl_val = data.duplicated().any()
# print(dupl_val)

# dropping duplicated values
data = data.drop_duplicates()

# checking again for duplicated value after deleting
dupl_val1 = data.duplicated().any()
# print(dupl_val1)


# ==== Find out number of courses per subjects
# print(data.columns)
# print(data["subject"].value_counts())

# Graph
# sns.countplot(data['subject'])
# plt.xlabel = ("Subjects")
# plt.ylabel = ("No of courses per subject")
# plt.show(rotation=60)

# ==== For which levels Udemy is providing courses
# print(data.columns)
# print(data['level'].value_counts())

# ==== Display the count of paid and free courses
# print(data.columns)
# print(data['is_paid'].value_counts())

# ==== Which course has max lectures free or paid
# print(data.columns)
# data["is_paid_new"] = data['is_paid'].astype('int')
# # print(data["is_paid_new"].dtypes)
# print(data.groupby(["is_paid_new"]).mean())


# ==== Which course have higher number of Subscriber free or paid
# print(data.columns)
# sns.barplot(x="is_paid", y='num_subscribers', data=data)
# plt.show()


# ==== Which level has highest number of subscriber
# sns.barplot(x="level", y="num_subscribers", data=data)
# plt.show()

# ===== Display 10 most popular courses as per number of subscribers
# print(data.columns)
top_10 = data.sort_values(by='num_subscribers', ascending=False).head(10)
# print(top_10)

# sns.barplot(x='num_subscribers', y='course_title', data=top_10)
# plt.show()

# ===== find the course having maximum number of reviews
# print(data.columns)
# print(data[data['num_reviews'] == data['num_reviews'].max()]['course_title'])
# sns.barplot(x="subject", y='num_reviews', data=data)
# plt.show()


# ===== Does price affect number of reviews
# print(data.columns)
# changing the figure size
plt.figure(figsize=(15,3))
# sns.scatterplot(x='price', y='num_reviews', data=data)
# plt.show()


# === Find total number of courses related to python
# print(data.columns)
# print(len(data[data['course_title'].str.contains("python", case=False)]))


# ==== Display top 10 python courses as per number of subscriber
# print(data.columns)
# print(data[data['course_title'].str.contains('python', case=False)].sort_values(by="num_subscribers", ascending=False)['course_title'].head(10))
# python_course = data[data['course_title'].str.contains('python', case=False)].sort_values(by="num_subscribers", ascending=False).head(10)
# print(python_course)
#
# sns.barplot(x="num_subscribers", y="course_title", data=python_course)
# plt.show()


# === In which year the highest number of courses are posted
print(data.columns)
# print(data['published_timestamp'].dt.year)
data["Year"] = data['published_timestamp'].dt.year
# print(data["Year"])
# print(data.groupby(by='Year').count()['course_title'])

# sns.countplot("Year", data=data)
# plt.show()

# ==== Display Category wise count of posted subjects yearwise
print(data.groupby('Year')["subject"].value_counts())