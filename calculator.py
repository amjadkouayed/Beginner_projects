# print ("option 1 = +")
# print ("option 2 = -")
# print ("option 3 = x")
# print ("option 4 = ÷")
# print("q = Quit")
# option = 1
# while (option != "q"):
#     option = (input ("choose your Option: "))
#     if (option in [1,2,3,4]):
#         num1 = int (input ("choose your first number: "))
#         num2 = int (input ("choose your second number: "))
#     if (option == 1):
#         result = float (num1 + num2)
#         print (str (result) )
#     elif (option == 2):
#         result = float (num1 - num2)
#         print (str (result) )
#     elif (option == 3):
#         result =  float (num1 * num2)
#         print (str (result))
#     elif (option == 4):
#         result =  float (num1 / num2) 
#         print (str (result) )

    
# print ("goodbye")

#-------------------------------------------

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
operation= input("pick one operation ' + , - , ÷ , x : ")
first_number = int(input("choose your first number: "))
second_number = int(input("choose your second number: "))

def addition(num1, num2):
    return num1+num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2



if operation is "+":
    result = addition(first_number, second_number)
elif operation == "-":
    result = subtraction(first_number, second_number)
elif operation == "x":
    result = multiplication(first_number, second_number)
elif operation == "÷":
    result = division(first_number, second_number)
else:
    print("invalid choice")

print(f"your result is {result}")

