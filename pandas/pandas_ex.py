import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)
print()

print(type(df['W']))
print(type(df))
print()

print(df[['W', 'Z']])
print()

df['new'] = df['W'] + df['Y']
print(df)
print()

print(df[df['W'] > 0])

df.drop('E', axis=0)
print(df)
print()

df.drop('new', axis=1, inplace=True)
print(df)
print()

data = {'Company':['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales':[200, 120, 340, 124, 243, 350]}
df2 = pd.DataFrame(data)
print(df2)
print()

byComp = df2.groupby('Company')
print(byComp.mean())
print()
print(byComp.sum())
print()

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print(df.loc['G1'].loc[1])
print()

print(df.index.names)

# pd.read_csv()
