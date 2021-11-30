name = "Abhay"
age = 21

## METHOD 1: Concatenation
print("My name is " + name + ", and I am " + str(age) + " years old.")

## METHOD 2: F-strings (Python 3+)
print(f"My name is {name}, and I am {age} years old")

## METHOD 3: Join
print(''.join(["My name is ", name, ", and I am ", str(age), " years old"]))

## METHOD 4: modulus operator
print("My name is %s, and I am %d years old." % (name, age))

## METHOD 5: format(Python 2 and 3)
print("My name is {}, and I am {} years old".format(name, age))
