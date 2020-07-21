import pandas as pd
import numpy as np

data = pd.read_csv('f.csv', sep=';', decimal=',')
print(data)

print()
datafr = pd.DataFrame(data)
print(datafr)

print()
print(datafr.columns)

print()
print(datafr.values)