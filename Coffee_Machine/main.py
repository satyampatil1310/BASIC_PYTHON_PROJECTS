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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(choice):
    if resources["water"] >= (MENU[choice["ingredients"["water"]]]):
        pass
    else:
        print("Sorry there is not enough water.")
    if resources["milk"] >= (MENU[choice["ingredients"["milk"]]]):
        pass
    else:
        print('Sorry there is not enough milk.')
    if resources["coffee"] >= (MENU[choice["ingredients"["coffee"]]]):
        print(f"Insert Coins of worth {MENU[choice['cost']]}")
    else:
        print("Sorry there is not enough coffee.")


resources["cost"] = 0


def deduct_resources(choice):
    resources["cost"] += (paid - change)
    return 0


def report():
    print(resources)


choice = input("“What would you like? (espresso/latte/cappuccino):")

check_resources(choice)

quarters = int(input("insert quarters "))
dimes = int(input("insert dimes "))
nickles = int(input("insert nickles "))
pennies = int(input("insert pennies"))
paid = ((quarters*0.25)+(dimes*0.10)+(pennies*0.01)+(nickles*0.05))
if MENU[choice['cost']] == paid:
    deduct_resources(choice)
    print(f"Here is your {choice}. Enjoy!")
elif MENU[choice['cost']] > paid:
    change = round(paid-MENU[choice["cost"]],2)
    print(f"“Here is {change} dollars in change.")
    deduct_resources(choice)
    print(f"Here is your {choice}. Enjoy!")
else:
    print("Sorry that's not enough money .")


