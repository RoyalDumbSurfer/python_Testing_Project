num = int(input())
exponent = 2
power = 1
while exponent <= num:
    exponent *= 2
    power += 1

print(exponent // 2, power - 1)
