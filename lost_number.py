n = int(input())
summ = 0
for i in range(1, n + 1):
    summ += i

for i in range(n - 1):
    summ -= int(input())
print(summ)
