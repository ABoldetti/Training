import pandas as pd
import numpy as np

a=pd.read_csv("/Users/andreaboldetti/Documents/projects/just-learning/python/data.csv")
c=a.peppo.to_numpy
# print(c)
# print(a.index)
print(a.columns)
print(a.columns[0])