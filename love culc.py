print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
combined_names_lower = combined_names.lower()

t = combined_names_lower.count('t')
r = combined_names_lower.count('r')
u = combined_names_lower.count('u')
e = combined_names_lower.count('e')
true = t + r + u + e

l = combined_names_lower.count('l')
o = combined_names_lower.count('o')
v = combined_names_lower.count('v')
e = combined_names_lower.count('e')
love = l + o + v + e

love_index = int(str(true) + str(love))

if (love_index) < 10 or (love_index) > 90:
    print(f"Your score is {love_index}, you go together like coke and mentos.")
elif 40 <= love_index <= 50:
    print(f"Your score is {love_index}, you are alright together.")
else:
    print(f"Your score is {love_index}.")
