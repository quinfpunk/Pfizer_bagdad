import pandas as pd
import numpy as np

distances = pd.read_excel('distances.xlsx', index_col=0, skiprows=1, usecols=range(1, 6))
print(distances)
index_value = pd.read_excel('indexValues.xlsx', header=None, names=["indexValue"], usecols=[1])
print(index_value)
