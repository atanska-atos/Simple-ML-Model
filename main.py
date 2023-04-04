# required libraries
import pandas as pd

import graph
import train_model
import prepare_data
from prepare_data import *
from train_model import *
from graph import *

# prepare a dataset
dataset = pd.read_csv("bodyfat.csv")

# show information about data in this dataset and prepare data for next steps
print("Would you like to see a data? [y/n]")
ans = input()
if ans.lower() == "y":
    prepare_data.print_data(dataset)

# create input from user side
value = int(input("Please, text value of ankle: "))
ankle = {'Ankle': [float(value)]}

# use a model
approximate_neck, fitted_model = train_model.create_and_train_model(dataset, ankle)

# graph of a result
graph.create_graph(dataset, fitted_model)

# print a result
print(f"If ankle have size {ankle['Ankle'][0]}, neck would be {round(approximate_neck[0], 2)}.")
