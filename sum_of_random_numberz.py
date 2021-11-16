from random import randint

x = 0
count = []
while randint(0, 10) != 0:
    x += 1
    count.append(x)

print(count)
print(sum(count))
