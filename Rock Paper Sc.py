import random

rock_2 = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_3 = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_1 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [scissors_1, rock_2, paper_3]

print("Let's play!")
user_name = input("What's your name?\n")
print(f"Welcome to the Game, {user_name}!")

user_choice = int(input("Choose one of the options: type '1'- scissors, type '2' - rock, type '3' - paper\n"))
print(f"{user_name} choice:\n")
print(game_images[user_choice])

ai_choice = random.randint(1, 3)
print("AI choice:\n")
print(game_images[ai_choice])

if ai_choice == user_choice:
    print(f"Draw. Let's play again, {user_name}!  🤷🏻‍")
elif ai_choice == 1 and user_choice == 2:
    print(f"You Win, {user_name}! Congratulations!!! 🤴🏻")
elif ai_choice == 1 and user_choice == 3:
    print(f"You Lose, {user_name}! 🥱")
elif ai_choice == 2 and user_choice == 1:
    print(f"You Lose, {user_name}! 🥱")
elif ai_choice == 2 and user_choice == 3:
    print(f"You Lose, {user_name}! 🥱")
elif ai_choice == 3 and user_choice == 1:
    print(f"You Win, {user_name}! Congratulations!!! 🤴🏻")
elif ai_choice == 3 and user_choice == 2:
    print(f"You Lose, {user_name}! 🥱")
else:
    print(f"You typed an invalid number, {user_name}!")
