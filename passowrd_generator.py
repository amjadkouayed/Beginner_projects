import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
number_of_letters= int(input("How many letters would you like in your password?\n")) 
number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_numbers = int(input(f"How many numbers would you like?\n"))

password= ""

for x in range(1, number_of_letters+1):
    password+= random.choice(letters)

for x in range(1, number_of_symbols+1):
    password+= random.choice(symbols)
    

for x in range(1, number_of_numbers+1):
    password+= random.choice(numbers)

password_charactars = list(password)
random.shuffle(password_charactars)
shuffled_password = "".join(password_charactars)


print(shuffled_password)

