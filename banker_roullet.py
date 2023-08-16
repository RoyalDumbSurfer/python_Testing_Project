import random

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(',')

pay_bill_index = random.randint(0, len(names) - 1)
pay_bill_name = names[pay_bill_index]
print(f"{pay_bill_name} is going to buy the meal today!")
print(list(map(list, pay_bill_name)))

# pay_bill = random.choice(names)
# print(f"{pay_bill} is going to buy the meal today!")

