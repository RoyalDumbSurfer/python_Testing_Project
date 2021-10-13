def row3(a, b):
    if isinstance(a, int) and isinstance(b, int) and a > b:
        for i in range(a, b - 1, -1):
            if i % 2 != 0:
                print(i, end=' ')
    else:
        print('wrong numbrs')
        exit()


row3(10, 3)
