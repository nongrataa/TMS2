import pandas as pd
import numpy as np

data = pd.read_csv('ff.csv', sep=';', decimal=',')
print(data)


print()
df = pd.DataFrame(data)
print(df)

print()
df.drop(1,axis=0,inplace=True)
print(df)

print()
del df['b']
print(df)