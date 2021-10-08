num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

count = []

if num_1:
    count.append(num_1)
if num_2:
    count.append(num_2)
if num_3:
    count.append(num_3)

print(min(count))
