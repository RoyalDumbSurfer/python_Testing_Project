x_first_day_run = int(input())
y_kilo_run_in_total = int(input())
count_days = 1

while x_first_day_run < y_kilo_run_in_total:
    x_first_day_run *= 1.1
    count_days += 1

print(count_days)
