sum_of_even = 0
for i in range(0, 101, 2):
    sum_of_even += i

print("-------------\n")
print(sum_of_even)



sum_of_even_2 = 0
for number in range(0, 101):
    if number % 2 == 0:
        sum_of_even_2 += number

print("-------------\n")
print(sum_of_even_2)
