import math
import random
import time

import seaborn as sns
import pickle


# df = sns.load_dataset("tips")
# file = "file.pkl"
# serilized process converting df object to binary format and saving into file
# pickle.dump(df,open(file, 'wb'))

# Deserilizing the pickeed object

# data = pickle.load(open(file, "rb"))
# print(data)



class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def describe(self):
        print(self.name, self.calories, sep=' : ')

#creating instance of clss Fruit
# fruit = Fruit('Banana', 200)
# # fruit.describe()
# # pickle_file = "fruits.pickle"
# # pickle.dump(fruit, open(pickle_file, "wb"))

# f = pickle.load(open('fruits.pickle', 'rb'))
# f.describe()
# f.calories = 250
# f.describe()






