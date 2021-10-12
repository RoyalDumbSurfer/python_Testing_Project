def bank(p, x, y):
    money_before = 100 * x + y
    money_after = int((money_before * p) / 100 + money_before)
    print(money_after // 100, '.', money_after % 100)


bank(100, 17, 34)
