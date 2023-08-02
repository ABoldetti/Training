import pandas as ps
import numpy as np
a=ps.read_csv("dati.csv")
b=ps.read_csv("errori.csv")
c=a.to_numpy()
d=b.to_numpy()
print(c, d)
