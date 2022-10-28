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

import random

print("Welcome to the Rock,Paper,Scissors game!")
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer = random.randint(0, 2)

defeat = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

match = {0: "rock", 1: "paper", 2: "scissors"}

art = {0: rock, 1: paper, 2: scissors}

if defeat[match[user]] == match[computer]:
    print(f"You gave:\n{art[user]}\nComputer gave:\n{art[computer]}\nYOU WIN!")
elif user == computer:
    print(f"You gave:\n{art[user]}\nComputer gave:\n{art[computer]}\nIT IS A DRAW.")
else:
    print(f"You gave:\n{art[user]}\nComputer gave:\n{art[computer]}\nYOU LOSE.")
