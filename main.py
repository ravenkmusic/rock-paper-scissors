rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choices = [rock, paper, scissors]
num_choices = len(choices)

users_choice = choices[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))]

computer_choice = choices[random.randint(0, num_choices)]

if users_choice == computer_choice:
  print(f"You both chose {str(computer_choice)}. It's a draw.")
if users_choice == 0 and computer_choice == 2:
  print("You win.")
else:
    print(f"Computer chose {computer_choice}. You lose.")
if users_choice == 1 and computer_choice == 0:
  print("You win.")
else: ("you lose.")
if users_choice == 2 and computer_choice == 1:
  print("You win.")
else:
  print("You lose.")