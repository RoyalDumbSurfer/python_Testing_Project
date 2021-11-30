list1 = ['karl', 'lary', 'keera']
list2 = [28934, 28935, 28936]

# Method 1: zip()
dictt0 = dict(zip(list1, list2))
print(dictt0)

# Method 2: dictionary comprehension
dictt1 = {key: value for key, value in zip(list1, list2)}
print(dictt1)

