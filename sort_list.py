list1 = ["Karl", "Larry", "Ana", "Zack"]

# Method 1: sort()
list1.sort()
print(list1)


# Method 2: sorted()
sorted_list = sorted(list1)
print(sorted_list)


# Method 3: Brute Force Method
size = len(list1)
for i in range(size):
    for j in range(size):
        if list1[i] < list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
print(list1)
