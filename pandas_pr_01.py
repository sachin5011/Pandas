"""
Data Analysis :
Data Analysis is a process of inspecting, cleansing,
transforming data with goal of discovering useful, information,
conclusions, and supporting decision-making.

Data Structures in Pandas
1. series
2. DataFrame
3.Pannel
"""

import pandas as pd
# x = [1,2,3,7,5,6]
# s = pd.Series(x)
# print(s)

#Dataframe in pandas
x = [1,2,3,7,5,6]
# df = pd.DataFrame(x)
# print(df)

# s_dict = {
#     "name" : ["Rahul", "Deepak", "Sam", "Partiv"],
#     "marks" : [1,2,3,4]
# }
# df = pd.DataFrame(s_dict)
# print(df)
# print(df.columns)
# print(pd.DataFrame(s_dict, columns=['name']))


# Arithematic operations

s = {
    "a" : [1,3,6,8,4],
    "b" : [4,6,2,9,1]
}

df = pd.DataFrame(s)
print(df)

# Adding row values and storing them to c column
# df["c"] = df['a']+df["b"]
# print(df)

# Substracting row values and storing them to c column
# df["c"] = df['a']-df["b"]
# print(df)

# Multiplying row values and storing them to c column
# df["c"] = df['a']*df["b"]
# print(df)


# df["Greater"] = df['a'] <= df["b"]
# print(df)

# Deleting and Inserting data into dataframe
# Insertion
# syntax : df.insert(index,column_name, data)
# df.insert(1, "C", df["a"]+10)
# print(df)
# df.insert(3, "SUM", df['a']+df['b']+df["C"])
# print(df)
df["new_column"] = df['a'][0:3]
# print(df)


# DELETION
# print("original df", df)
# deleted_column = df.pop("new_column")
# print("after deletion",df)
# print(deleted_column)



# CSV in pandas
# print(df)
# file = df.to_csv("dataframe.csv", index=False, header=["first", 'second', 'third'])

data = pd.read_csv('dummy.csv')
# print(data)
print(data.columns)

# getting the first n row data
data1 = pd.read_csv('dummy.csv', nrows=2)
# print(data1)

# getting specic rows of data
# print (data[3:6])
# getting specific columns from csv file
# data23 = pd.read_csv('dummy.csv', usecols=['Period','Data_value','Suppressed'])
# print(data23)

# Skipping rows in csv file
# data2 = pd.read_csv('dummy.csv', skiprows=[0,3,4,5])
# print(data2)


# Declearing column as index
# data3 = pd.read_csv('dummy.csv', index_col=['Data_value'])
# print(data3)

# changing heading of columns
# data4 = pd.read_csv('dummy.csv', header=2)
# print(data4)

# changing the datatype of a column
# data5 = pd.read_csv('dummy.csv', dtype={"Data_value":str})
# print(type(data5["Data_value"]))

# getting all data from csv file
# print(data.describe())

# To make changes in dataframe column
# data.loc[0, "Series_reference"] = "Changed Value"
# print(data[:3])

# getting the data of specific column and row
# dt = data.loc[[1,3], ["Series_reference", "Series_title_4"]]
# print(dt)  # this will print row 1 and 3 data of column "Series_reference", "Series_title_4"

# val = data.iloc[0,1]
# print(val)  # this will accept the indexes of row and column and gives the specific value


#     Handling Missing Data
# dropena and fillna



