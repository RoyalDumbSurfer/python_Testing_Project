def day_time(n):
    h = 60
    all_day = 1440
    if n > all_day:
        print('too big')
    else:
        if n < h > 0:
            print('0', ':', n)
        if n > h < all_day:
            print(n // h, ':', n % h)


day_time(1439)
