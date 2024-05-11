MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

user = ""


def type_of_coffee():
    user = input("What would you like? (espresso/latte/cappuccino):")
    if user == "report":
        return True
    elif user=="espresso" or user=="latte" or user=="cappuccino":
        for i in resources:
            if resources[i] > MENU[user]["ingredients"][i]:
                return user
            elif resources[i] < MENU[user]["ingredients"][i]:
                return f"Sorry there is not enough {i}."
                break
    else:
        quit()


profit = 0
penny = 0.01
nickel = 0.05
dine = 0.1
quarter = 0.25

total = 0


def check():
    global total
    user_input = type_of_coffee()
    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        print("Please insert coins:")
        a = int(input("How many quarters?:"))
        b = int(input("How many dines?:"))
        c = int(input("How many nickels?:"))
        d = int(input("How many pennies?:"))
        profit = (a * quarter) + (b * dine) + (c * nickel) + (d * penny)
        change = profit - MENU[user_input]["cost"]
        if profit < MENU[user_input]["cost"]:
            print("Sorry that's not enough money. Money refunded")
        elif profit >= MENU[user_input]["cost"]:
            total += MENU[user_input]["cost"]
            print(f"Here is ${round(change, 2)} in change")
            print(f"Here is your {user_input}!")
            for i in MENU[user_input]["ingredients"]:
                resources[i] = resources[i] - MENU[user_input]["ingredients"][i]
    elif user_input == True:
        resources["Money"] = total
        for i, j in resources.items():
            print(f"{i}: {j}")
    else:
        print(user_input)
    check()

check()
