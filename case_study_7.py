import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


pd.set_option("display.max_column", None)

data = pd.read_csv(".\case_study_datasets\\top-5000-youtube-channels.csv")

# ==== Display All rows except last 5 rows using head method
# print(data.head(-5))

# ==== Display All rows except first 5 rows using head method
# print(data.tail(-5))

# ==== Find the shape of the dataset(number of rows and column)
# print(data.shape)
# print("Number of rows : ",data.shape[0])
# print("Number of columns : ",data.shape[1])

# ==== Get the information about the dataset like number of rows and column, datatype and memory used
# print(data.info())

# ===== Get over all statistics about the dataset
# print(data.describe(include='all'))

# ===== Data Cleansing (Replace -- to NaN)
# print(data.replace("--", np.nan, regex=True))


# CHeck null values in dataset
# print(data.isnull().sum())

# Data Cleansing
# print(data.head())
# 1. first we are going to clean rank column
# data["Rank1"] = data["Rank"].replace(data)
data["Rank1"] = data['Rank'].str[:-2]
# print(data["Rank1"])
data['Rank2'] = data["Rank1"].str.replace(",", "")
# print(data["Rank2"])
data["Rank"] = data["Rank2"].astype("int")
# print(data["Rank"])
# print(data["Rank"].mean())

# 2. cleaning Video Uploads
data["Video Uploads"] = data["Video Uploads"].replace("--", 0)
data["Video Uploads"] = data["Video Uploads"].astype('int')
# print(data["Video Uploads"].dtypes)

# 3. Cleaning Subscribers column
data["Subscribers"] = data["Subscribers"].replace("-- ",0)
data["Subscribers"] = data["Subscribers"].astype("int")

# 4. Cleaning Grade column
# ----> a . getting unique valuews for thius column
# print(data["Grade"].unique())
data["Grade"] = data["Grade"].map({'A++ ':5, 'A+ ':4, 'A ':3,   'A- ':2,  'B+ ':1, '\xa0 ':0})
# print(data["Grade"])
# print(data.dtypes)
# print(data.head())

# ====== Find the average views for each channel
# print(data.columns)
data["Avg_views"] = data["Video views"]/data["Video Uploads"]
# print(data.head())

# ====== Find top 5 channels having max number of uploads
# print(data.columns)
# print(data["Video views"].sort_values(ascending=False).head())
# or
# print(data.sort_values(by="Video Uploads", ascending=False)[["Channel name", "Video Uploads"]].head())

# ===== Find correlation Matrix
# print(data.corr())

# ====== Which grade has maximum number of Video Uploads
# print(data.columns)
# print(data[data['Video Uploads'] == data['Video Uploads'].max()]["Grade"])
# sns.barplot(x="Grade", y="Video Uploads", data=data)
# plt.show()

# ====== Which grade has highest number of Views
# sns.barplot(x="Grade", y="Video views", data=data)
# plt.show()

# ====== Which Grade has Highest number of Subscriber
# sns.barplot(x="Grade", y="Subscribers", data=data)
# plt.show()

# ===== Which grade has Average number of views
# print(data.columns)
# sns.barplot(x="Grade", y="Avg_views", data=data)
# plt.show()

