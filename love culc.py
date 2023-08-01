print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower = name1.lower()
name2_lower = name2.lower()

counter_1 = 0
if name1_lower.count('t'):
    counter_1 += name1_lower.count('t')
if name1_lower.count('r'):
    counter_1 += name1_lower.count('r')
if name1_lower.count('u'):
    counter_1 += name1_lower.count('u')
if name1_lower.count('e'):
    counter_1 += name1_lower.count('e')

if name2_lower.count('t'):
    counter_1 += name2_lower.count('t')
if name2_lower.count('r'):
    counter_1 += name2_lower.count('r')
if name2_lower.count('u'):
    counter_1 += name2_lower.count('u')
if name2_lower.count('e'):
    counter_1 += name2_lower.count('e')

counter_2 = 0
if name1_lower.count('l'):
    counter_2 += name1_lower.count('l')
if name1_lower.count('o'):
    counter_2 += name1_lower.count('o')
if name1_lower.count('v'):
    counter_2 += name1_lower.count('v')
if name1_lower.count('e'):
    counter_2 += name1_lower.count('e')

if name2_lower.count('l'):
    counter_2 += name2_lower.count('l')
if name2_lower.count('o'):
    counter_2 += name2_lower.count('o')
if name2_lower.count('v'):
    counter_2 += name2_lower.count('v')
if name2_lower.count('e'):
    counter_2 += name2_lower.count('e')

counter_1_str = str(counter_1)
counter_2_str = str(counter_2)

love_index = int(counter_1_str + counter_2_str)

if love_index < 10 or love_index > 90:
    print(f"Your score is {love_index}, you go together like coke and mentos.")
elif 40 < love_index < 50:
    print(f"Your score is {love_index}, you are alright together.")
else:
    print(f"Your score is {love_index}.")


