def sum_of_fac():
    n = int(input())
    part_fac = 1
    res_fac = 0
    if n < 0:
        print('wrong number')
    else:
        for i in range(1, n + 1):
            part_fac *= i
            res_fac += part_fac
    print(res_fac)


sum_of_fac()
