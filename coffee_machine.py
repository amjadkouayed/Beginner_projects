MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

""" 
we are making a coffee machine 
1- Prompt user by asking “ What would you like? options: chooses the type of coffee, OFF(powers off machine), report(prints the recoures)
2- check resources sufficiency 
3- process coins
4- check if the money is sufficient 
5- make the coffee and deduct from the recourses 

"""

def check_resources(drink): #checks suffitient resources in the achine
    for item in drink:
        if drink[item] < resources[item]:
            return True
        else:
            print(f"sorry there's not enough {item}")
            return False


def proccess_money(quarters):
    proccessed = int(quarters) * 0.25
    return proccessed

def check_transaction(drink, money): #check if the transaction is successful and calculates change and profit
    global change
    global profit
    if money < drink["cost"]:
        print("sorry not enough money")
        return False
    elif money >= drink["cost"]:
        change = money - drink["cost"]
        profit += drink["cost"]
        print(f"here's your change {change}")
        return True
    
def make_coffee(drink_name, drink_ingredients): # deduct the ingriedents from the resources 
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"here's your {drink_name} boss ☕")

change = 0

power_on = True

while power_on:
    customer_input = input("What would you like? (espresso/latte/cappuccino):")
    
    if customer_input == "off":
        power_on = False
    elif customer_input == "report":
        print(f"water: {resources['water']}\nmilk = {resources['milk']}\ncoffee = {resources['coffee']}\nmoney = ${profit}")
    else:
        drink = MENU[customer_input]
        if check_resources(drink["ingredients"]):
            print("please insert money")
            quarters = input("how many quarters have you insterted?")
            amount_paid = proccess_money(quarters)
            if check_transaction(drink, amount_paid):
                make_coffee(customer_input, drink["ingredients"])
            
        else:
            print("not enough recourses")