num = int(input())
dev_num = 2

if num < 2:
    print('wrong number')
    exit()
else:
    while num % dev_num != 0:
        dev_num += 1
print(dev_num)
