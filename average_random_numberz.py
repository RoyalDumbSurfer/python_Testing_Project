from random import randint

x = randint(0, 10)
y = []

while x != 0:
    y.append(x)
    x = randint(0, 10)
print(y)
print(sum(y) / len(y))
