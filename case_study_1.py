import pandas as pd

data = pd.read_csv(".\case_study_datasets\Ecommerce Purchases.txt")
# print(data.head(10))
# print(data.tail(10))

# print(data.info())

# print(data.isnull().sum())

# ===== Highest and lowes purchase price
# print("Highest Purchase Price  : ",data["Purchase Price"].max())
# print("Minimun Purchase Price  : ",data["Purchase Price"].min())

# ===== Average Purchase Price
# print("Average Purchase Price : ",data["Purchase Price"].mean())

# ===== People Having fr as language
# print(len(data[data["Language"].isin(["fr"])]))


# ===== Find the job title contains engineer
# print(data[data['Job'].str.contains('engineer', case=False)])
# this will count all the job title having engineer in title
# print(len(data[data['Job'].str.contains('engineer', case=False)]))

# ===== FInd the emails with this ip 132.207.160.22
# print(data[data['IP Address'] == "132.207.160.22"]["Email"])

# ===== How many people have mastercard as creditcard provider and made a purchase above 50
# print(data.columns)
# print(data[(data["CC Provider"] == "Mastercard") & (data["Purchase Price"] > 50)])
# print(len(data[(data["CC Provider"] == "Mastercard") & (data["Purchase Price"] > 50)]))

# ===== Find the email of the person with following creditcard number 4664825258997302
# print(data.info())
# print(data[data['Credit Card'] == 4664825258997302]['Email'])

# ===== Find the number of people purchase During the AM and PM
# print(data.columns)
# print("Total AM purchase : ",len(data[data["AM or PM"] == "AM"]))
# print("Total PM purchase : ",len(data[data["AM or PM"] == "PM"]))
# best way
# print(data["AM or PM"].value_counts())

# ===== How many people having credit card expiring in 2020
# print(data.columns)
# def checkExp():
#     count = 0
#     for val in data["CC Exp Date"]:
#         if val.split('/')[1] == "20":
#             count += 1
#     return count
# print(checkExp())
# # or
# print(len(data[data["CC Exp Date"].apply(lambda x : x[3:] == "20")]))


# ===== Find top 5 email provider ie gmail.com, yahoo.com etc

# def getextension():
#     ext_lst = []
#     for email in data["Email"]:
#         ext_lst.append(email.split('@')[1])
#     return ext_lst
#
# data['temp_email'] = getextension()
# print(data["temp_email"].value_counts().head(5))

# BEST WAY
# print(data["Email"].apply(lambda x : x.split("@")[1]).value_counts().head(5))


