'''Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.'''  

# import sys
# import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# print("welcome to the rock, paper, scissors game")

# user_choice = input("choose rock, paper, scissors\n").lower()
# choices = [rock,paper,scissors]
# computer_choice = random.choice(choices)
# user_output = 0

# if user_choice == "rock" :
#     user_output = rock
# elif user_choice == "paper":
#     user_output = paper
# elif user_choice == "scissors":
#     user_output = scissors
# else:
#      print(" invalid input")
#      sys.exit()

# print(user_output)
# print("computer choice" + computer_choice)

# if user_output == rock and computer_choice == scissors:
#     print ("you win")
# elif user_output == scissors and computer_choice == paper:
#         print ("you win")
# elif user_output == paper and computer_choice == rock:
#     print ("you win")
# elif user_output == computer_choice:
#      print("it's a draw")
# else:
#     print("you lose")

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock. 

import sys
import random
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

print("welcome to the Rock Paper Scissors game\n")
choices = { 
     "rock": rock,
     "paper": paper,
     "scissors": scissors
}

user_input = input("choose your option Rock, Paper, Scissors\n").lower()

if user_input not in choices:
    print ("invalid input")
    sys.exit()

computer_input = random.choice(list(choices.keys()))

print("you choose")
print(choices[user_input])
print("computer chooses")
print(choices[computer_input])

if user_input == computer_input:
     print("its a draw")
elif (
     (user_input == "rock" and computer_input == "scissors" ) or
     (user_input == "scissors" and "computer_input" == paper) or
     (user_input == "paper" and "computer_input" == rock)
    ):
    print (" you win ")
else:
    print("you lose")



# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock. 