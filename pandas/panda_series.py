import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']

mylist = [11, 21, 31]

arr = np.array([12, 22, 32])

d = {'a': 13, 'b': 23, 'c': 33}
print(pd.Series(data=mylist))
new_series = pd.Series(data=mylist, index=labels)
new_series = pd.Series(mylist, labels)
print(new_series)

print(pd.Series(arr, labels))

print(pd.Series(d))

salesQ1 = pd.Series(data=[250, 450, 200, 150], index=[
                    'USA', 'China', 'India', 'Brazil'])
print(salesQ1)

salesQ2 = pd.Series(data=[260, 500, 210, 100], index=[
                    'USA', 'China', 'India', 'Japan'])
print(salesQ2)

print(salesQ2['China'])
print(salesQ2[0])
