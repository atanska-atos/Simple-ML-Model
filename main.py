# required libraries

import pandas as pd

# load data from CSV file

dataset = pd.read_csv("bodyfat.csv")


# print information about dataset

size = dataset.size
columns = [col for col in dataset.columns]
num_cols = dataset.shape[1]
num_rows = dataset.shape[0]

print(f"Training dataset has {dataset.size} records.")
print(f"There are {num_cols} columns: {columns} and {num_rows} rows.\n")
print("Under is presented first 5 rows in this dataset:")
print(dataset.head())


# data filtration by columns

del dataset['Density']
del dataset['BodyFat']
del dataset['Age']
del dataset['Weight']
del dataset['Height']
del dataset['Chest']
del dataset['Abdomen']
del dataset['Hip']
del dataset['Thigh']
del dataset['Knee']
del dataset['Biceps']
del dataset['Forearm']
del dataset['Wrist']

print("\nFirst five records after filtration:")
print(dataset.head())
print(f"Now table has {dataset.shape[1]} columns.")