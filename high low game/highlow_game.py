from data import data
import random
from art import *

"""
a game where the user chooses between 2 account, if the account he chooses has more followers the game continues
and one point is added to the choice

1- format the data in the dicionary to show only name occupation, country
1- def a funktion that seleects two option from the data
2- define a funktion that chooses the most popular one 
3- assign the option to variables 
4- print the logo and VS logo,
5- have a score count
6- give feedback on their answer
7- make the account at position b move to position a 
8- clear the screen between rounds

"""

score = 0
gameover = False
choice_B = random.choice(data)

while gameover == False:

    #chooces a random option from the list
    choice_A = choice_B
    choice_B = random.choice(data)
    if choice_A == choice_B:
        choice_B = random.choice(data)


    # format the account data, any of the choices as an input
    def formatting(account):
        account_name = account['name']
        account_desc = account['description']
        account_country = account['country']
        return (f"{account_name} a {account_desc} from {account_country}")


    choice_A = formatting(choice_A)
    choice_B = formatting(choice_B)



    #defines wich one with the more followers
    def correct(a,b):
        if a > b: 
            return 'a'
        else: 
            return 'b'


    print(logo)
    print(f"compare A: {choice_A}")
    print(vs)
    print(f"againt B: {choice_B}")

    guess = input("who has more follower type A or B : ").lower()

    if guess == correct(choice_A, choice_B):
        score += 1
        print(f"you're right, your score is {score}")
    else:
        gameover = True
        print(f"Game Over, your final score is {score}")
        