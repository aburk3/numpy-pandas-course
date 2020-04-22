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


# Access index from data-frame
# print(df.loc['A'])
# print(df.loc[['A']])

# print(df)
# print(df.loc[['A', 'E']])
# print(df.iloc[0:3])
# print(df.drop('C'))
# print(df.loc[['A', 'C'], ['W', 'Y']])

"""
    Conditional Selections in Pandas
"""
# print(df[df > 0])

# Grab all rows where X is greater than zero
# print(df[df['X'] > 0])

"""
    Multiple conditionals
"""
# Where both conditions are True
# value = df[(df['W'] > 0) & (df['Y'] > 1)]
# print(value)

# Resetting an index
# value = df.reset_index()
# print(df)
# print(value)

# Setting a column as an index
new_ind = ['CA', 'NY', 'WY', 'OR', 'CO']
df['States'] = new_ind
print(df)
value = df.set_index('States')
# States is not a column, but the name of the index - as indicated by the spacing.
print(value)
print(value.columns)
print(df.describe())
