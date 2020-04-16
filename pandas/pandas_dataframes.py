import numpy as np
import pandas as pd

from numpy.random import randint

columns = ['W', 'X', 'Y', 'Z']

index = ['A', 'B', 'C', 'D', 'E']

# Set seed to get SAME random numbers
np.random.seed(42)
data = randint(-100, 100, (5, 4))
print(data)
