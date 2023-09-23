import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for i in range(len(chosen_word)):
    display.append('_')
print(display)

guess = input("Guess a letter: \n").lower()

count_index = 0
for letter in chosen_word:
    count_index += 1
    if letter == guess:
        del display[count_index-1]
        display.insert(count_index-1, guess)

print(display)
