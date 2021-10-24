num = int(input())
fnum = 1
count = []
if num < 0:
    print('wrong number')
    exit()
else:
    for i in range(1, num + 1):
        fnum *= i
        count.append(fnum)
print(count)
print(fnum)
