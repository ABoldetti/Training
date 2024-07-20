import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tabula as tb
import os

os.chdir('~/file')
files = os.listdir()

for i in files:
    df = tb.read_pdf(os.cwd() + i , pages = "all")[0]


a = df.columns

df = df.rename(columns = {a[0]: "matricola" , a[1]: "1", a[2]: "2", a[3]: "voto" , a[4]: "passato"})

df.loc[len(df)] = a
for i in range( len(df)):
    df._set_value( index=i, col='voto' , value = float(df['voto'][i].replace( "," , "." ))) 

df.to_csv("algebra.csv")

