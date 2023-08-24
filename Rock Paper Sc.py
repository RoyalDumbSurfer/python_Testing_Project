import random

scissors_0 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_1 = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_2 = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

game_images = [scissors_0, rock_1, paper_2]

print("Let's play!")
user_name = input("What's your name?\n")
print(f"Welcome to the Game, {user_name}!")

user_choice = int(input("Choose one of the options: type '0'- scissors, type '1' - rock, type '2' - paper\n"))
ai_choice = random.randint(0, 2)

if user_choice > 2 or user_choice < 0:
    print(f"You typed an invalid number, {user_name}!")
else:
    print(f"{user_name} choice:\n")
    print(game_images[user_choice], "\n")
    print("AI choice:\n")
    print(game_images[ai_choice])


if ai_choice == user_choice:
    print(f"Draw. Let's play again, {user_name}!  🤷🏻‍")
elif ai_choice == 0 and user_choice == 1:
    print(f"You Win, {user_name}! Congratulations!!! 🤴🏻")
elif ai_choice == 0 and user_choice == 2:
    print(f"You Lose, {user_name}! 🥱")
elif ai_choice == 1 and user_choice == 0:
    print(f"You Lose, {user_name}! 🥱")
elif ai_choice == 1 and user_choice == 2:
    print(f"You Win, {user_name}! Congratulations!!! 🤴🏻")
elif ai_choice == 2 and user_choice == 0:
    print(f"You Win, {user_name}! Congratulations!!! 🤴🏻")
elif ai_choice == 2 and user_choice == 1:
    print(f"You Lose, {user_name}! 🥱")

