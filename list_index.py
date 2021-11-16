from random import randint

x = randint(0, 100)
y = []

while x != 0:
    y.append(x)
    x = randint(0, 100)

print(y)
print(max(y))
z = max(y)
print(y.index(z))
