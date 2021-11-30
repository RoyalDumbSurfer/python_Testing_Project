maths = [59, 64, 75, 86]
physics = [78, 98, 56, 56]

# Brute Force Method
list1 = [
    maths[0] + physics[0],
    maths[1] + physics[1],
    maths[2] + physics[2],
    maths[3] + physics[3]
]
print(list1)

# List Comprehension
list1 = [x + y for x, y in zip(maths, physics)]
print(list1)

# Using Maps
import operator

all_devices = list(map(operator.add, maths, physics))
print(all_devices)

# Using Numpy Library
import numpy as np

list1 = np.add(maths, physics)
print(list1)
