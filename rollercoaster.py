print("Welcome to roller coaster!")
height = int(input("How tall are you in cm? "))
bill = 0

if height < 120:
    print("Can't ride buddy, sorry:)")
else:
    age = int(input("How old are you? "))
    if age < 12:
        bill += 5
    elif 12 < age < 18:
        bill += 7
    elif 18 < age < 45 or age > 55:
        bill += 12
    want_foto = input("Want foto? Y or N ")
    if want_foto == "Y":
        bill += 3
    print(f"The total bill is ${bill}")
