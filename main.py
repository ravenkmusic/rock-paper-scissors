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

users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if users_choice >= 3 or users_choice <0:
  print("You have entered an invalid number. You lose.")
else:
  print(f"You chose: {choices[users_choice]}")

  computer_choice = random.randint(0, 2)
  print(f"Computer chose: {choices[computer_choice]}")

  if users_choice == 0 and computer_choice == 2:
    print("You win.")
  elif computer_choice == 0 and users_choice == 2:
      print("You lose.")
  elif users_choice > computer_choice:
      print("You win!")
  elif computer_choice > users_choice:
      print("You lose.")
  elif users_choice == computer_choice:
      print("You both chose the same thing. It's a draw.")