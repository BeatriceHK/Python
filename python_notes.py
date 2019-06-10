print "Hello, world!"
print(2+3)

height = 1.67
weight = 60
bmi = weight/(height**2)

# check out the type of a value
type(bmi)

day_of_week = 6
type(day_of_week)

x = "body mass index"
type(x)

z = True
type(z)

# sums of two integers, and sums of two strings
2+3
'ab'+'cd'

# 12.02.2016
# Create list baseball 
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

#%% 11.08.2017

import numpy as np
import pandas as pd

# build a vector containing an arithmetic progression
np.arange(10)

# create a data frame and specify the column names
df = pd.DataFrame({"pear": [1,2,3], "apple": [2,3,4], "orange": [3,4,5]})
df

len(df.columns) # count the number of columns

























