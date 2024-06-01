#Nnumber Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
print(""" 
                 _                                   _                                 
  _ _ _  _ _ __ | |__  ___ _ _   __ _ _  _ ___ _____(_)_ _  __ _   __ _ __ _ _ __  ___ 
 | ' \ || | '  \| '_ \/ -_) '_| / _` | || / -_|_-<_-< | ' \/ _` | / _` / _` | '  \/ -_)
 |_||_\_,_|_|_|_|_.__/\___|_|   \__, |\_,_\___/__/__/_|_||_\__, | \__, \__,_|_|_|_\___|
                                |___/                      |___/  |___/                
 """)

gameover = True
computer_number = random.randint(1,100)
print(" I'm thinking of a number between 1 to 100")
#print(f"pssssst number is {computer_number} ")
difficulty = input("choose difficulty 'Easy' or 'Hard' ")

def easy():
    global gameover
    attempts = 10
    print(f"you have {attempts} attempts left")
    while attempts > 0:
        guess = int(input("make a guess: "))
        if guess != computer_number:
            attempts = attempts - 1 
            if guess < computer_number:
                print(f" too low you have '{attempts}' attempts left")
            elif guess > computer_number:
                print(f"too high you have '{attempts}' attempts left")
        else:
            attempts = 0
            gameover = False


def hard():
    global gameover
    attempts = 5
    print(f"you have {attempts} attempts left")
    while attempts > 0:
        guess = int(input("make a guess: "))
        if guess != computer_number:
            attempts = attempts - 1 
            if guess < computer_number:
                print(f" too low you have '{attempts}' attempts left")
            elif guess > computer_number:
                print(f"too high you have '{attempts}' attempts left")
        else:
            attempts = 0
            gameover = False
        


if difficulty == "easy":
    easy()
elif difficulty == "hard":
    hard()
else:
    print("invalid choice")

if gameover :
    print(f"you lose computer number was {computer_number} ")
else:
    print("you won winner winner chicken dinner")

