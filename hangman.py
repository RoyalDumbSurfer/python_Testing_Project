import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 7
stages_index = 0

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for i in range(len(chosen_word)):
    display.append('_')
print(display)

while '_' in display:
    if lives == 0:
        print("GAME OVER")
        break
    guess = input("Guess a letter: \n").lower()
    if guess in display:
        print("You already guessed that letter. Guess again.")
    count_index = 0
    count_letters = chosen_word.count(guess)
    if count_letters:
        for letter in chosen_word:
            count_index += 1
            if letter == guess:
                del display[count_index - 1]
                display.insert(count_index - 1, guess)
    else:
        lives = lives - 1
        stages_index += 1
        print("There is no such letter in this word.")
        print(stages[-stages_index])

    print(f"Number of lives - {lives}")
    print(display)

if '_' not in display:
    print("You Win!!!")
