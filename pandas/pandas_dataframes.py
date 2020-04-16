import numpy as np
import pandas as pd

from numpy.random import randint

columns = ['W', 'X', 'Y', 'Z']

index = ['A', 'B', 'C', 'D', 'E']

# Set seed to get SAME random numbers
np.random.seed(42)
data = randint(-100, 100, (5, 4))
# print(data)

df = pd.DataFrame(data, index, columns)
# print(df)

# print(df['W'])

# In a dataframe, the columns are just a panda series
# print(type(df['W']))
# => type: pandas.core.series.Series
# print(type(df))
# => type: pandas.core.frame.DataFrame

# Double-bracket notation for multiple coulmns
# print(df[['W', 'Z']])

# Create new column from pre-existing data-frame
df['new'] = df['W'] + df['Y']

# Delete a column - not permanent
# print(df.drop('new', axis=1))
