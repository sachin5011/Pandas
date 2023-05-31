import pandas as pd

std_dict = {
    "name" : ["Santosh", "Sam", "Ayesha", "Ajay", "Shruti", "Somesh", "Vikram", "Bikesh", "Vaibhav", "Ramesh"],
    "marks"  : [77, 33, 89, 45, 78, 56, 67, 99, 92, 40],
    "gender" : ["Male", "Male", "Female", "Male", "Female", "Male", "Male","Male", "Male", "Male", ]
}

df = pd.DataFrame(std_dict)
# print(df.head())
# print(df.columns)

# === Displaying the number of columns and rows and memory and datatype of columns
# print(df.info())

# ==== Display top 3 data
# print(df.head(3))

# ===== Display last 3 data
# print(df.tail(3))

# === Getting the shape of dataframe number of rows*column
# print(df.shape)

# ==== Checking the null values in dataframe
# print(df.isnull())



# === Null value count column wise or axis=0
# print(df.isnull().sum(axis=0))


# === Null value count row wise or axis=1
# print(df.isnull().sum(axis=1))

# ==== Get overall Statistic about dataframe
# print(df.describe())
# print(df.describe(include="all"))

# ==== Getting the unique values from a column
# print(df['gender'].unique())

# ==== Getting number of unique values from a column
# print(df["gender"].nunique())

# ==== Getting the count of unique values from a column
# print(df['gender'].value_counts())

# ==== Getting count between a specific range
# print(df[df['marks']>=80])
# print(df[(df['marks']>50) & (df['marks']<70)])
# print(len(df[(df['marks']>50) & (df['marks']<70)]))
# print(df[df["marks"].between(50,70)])

# ==== Getting the average, min, max, sum of a column
# print(df["marks"].mean())
# print(df["marks"].max())
# print(df["marks"].min())
# print(df["marks"].sum())

# ==== Apply Methods(Function)

def gethalf(x):
    return x/2

# print(gethalf(df["marks"]))
df["half marks"]=df['marks'].apply(gethalf)
# print(df)

df["Double Marks"] = df['marks'].apply(lambda x:x*2)
# print(df)

# ==== Map Function
# changin Male to 1 and female to 0 using map function
df["male_female"]= df["gender"].map({"male" : "1", "female" : "0"})
# print(df)

# ===== Drop column from Dataframe
# It will drop male_female column
# print(df.drop("male_female", axis=1))

# print(df.drop(["half marks", "male_female"], axis=1))

# ==== Getting the name of all the coluymns
# print(df.columns)

# print(df.index)

# === Sorting the data asc or desc
# desc order
# print(df.sort_values(by='marks', ascending=False))
# asc order
# print(df.sort_values(by='marks'))

# ==== Display name, marks of female students
# print(df[df["gender"] == "Female"][["name", "marks"]])

# print(df[df['gender'].isin(['Female'])][['name', 'marks']])

