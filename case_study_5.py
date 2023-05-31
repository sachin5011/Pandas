import pandas as pd

pd.set_option("display.max_column", None)
data = pd.read_csv(".\case_study_datasets\googleplaystore.csv")
# print(data.head())

# ===== Display top 5 rows from dataset
# print(data.head(5))

# ===== Display last 5 rows from dataset
# print(data.tail(5))

# ===== Display the shape of the dataset (Number of rows and columns)
# print(data.shape)
# print("Number of rows : ", data.shape[0])
# print("Number of column : ", data.shape[1])

# ===== Get the information about dataset (Total number of rows and column, datatype and memory)
# print(data.info())

# ==== Get overall statistics about dataset
# print(data.describe(include='all'))

# ===== Total number of app title contain Astrology
# print(data.columns)
# print(len(data[data["App"].str.contains("Astrology", case=False)]))

# ==== Find the average app rating
# print(data.columns)
# print(data['Rating'].mean())


# ==== Find the total number of unique category
# print(data.columns)
# print(len(data['Category'].unique()))
# print(data['Category'].nunique())

# ==== Which category getting highest average rating
# print(data.columns)
# print(data.groupby('Category')['Rating'].mean().sort_values(ascending=False))

# ==== Find total number of apps having 5 start rating
# print(len(data[data['Rating'] == 5.0]))

# ===== Find the average value of reviews
# print(data.columns)
# print(data['Reviews'].dtype)
# to find average of object datatype we have to typecast
# there are asome string values in review column first we need to replace them
data['Reviews'] = data['Reviews'].replace('3.0M', 3.0, inplace=True)
# converting the values to float
data['Reviews'] = data['Reviews'].astype('float')
# print(data['Reviews'].dtype)
# print(data['Reviews'].mean())

# ===== Find total number of free and paid apps
# print(data.columns)
print(data['Type'].value_counts())
