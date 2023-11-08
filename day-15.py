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

money = 0

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05 
PENNIES = 0.01

def report():
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCofee: {resources['coffee']}g\nMoney: ${money}"
  

def check_resources(coffee):
    if coffee != "espresso":
       milk_q = MENU[coffee]["ingredients"]["milk"]
    water_q = MENU[coffee]["ingredients"]["water"]
    coffee_q = MENU[coffee]["ingredients"]["coffee"]


    if water_q > resources["water"]:
       print("Sorry there is not enough water.")
       return False
    elif coffee != "espresso" and milk_q > resources["milk"]:
       print("Sorry there is not enough milk.")
       return False
    elif coffee_q > resources["coffee"]:
       print("Sorry there is not enough coffee.")
       return False
    else:
       return True


def calculate_monetary(quarter, dime, nickle, pennie):
    total = (quarter * QUARTERS) + (dime * DIMES) + (nickle * NICKLES) + (pennie * PENNIES)
    return total


def drop_resources(type_of_coffee):
    if type_of_coffee != "espresso":
        resources["milk"] -= MENU[type_of_coffee]["ingredients"]["milk"]
    resources["water"] -= MENU[type_of_coffee]["ingredients"]["water"]
    resources["coffee"] -= MENU[type_of_coffee]["ingredients"]["coffee"]
   


shut_down = False
while shut_down != True:
  comand = input(" What would you like? (espresso/latte/cappuccino): ").lower()
  
  if comand == "report":
    print(report())
    continue
  elif comand == "off":
    print("Shut down")
    shut_down = True
    continue
  elif comand == "espresso":
     have_resourse = check_resources(comand)
  elif comand == "latte":
     have_resourse = check_resources(comand)
  elif comand == "cappuccino":
     have_resourse = check_resources(comand)

  if have_resourse:
     print("Please insert coins.")
     quarters = float(input("how many quarters?: "))
     dimes = float(input("how many dimes?: "))
     nickles = float(input("how many nickles?: "))
     pennies = float(input("how many pennies?: "))

     monetary = float(calculate_monetary(quarters, dimes, nickles, pennies))

  cost_comand = MENU[comand]["cost"]   
  if monetary < cost_comand:
     print("Sorry that's not enough money. Money refunded.")
  else:
     change = monetary - cost_comand
     print(f"Here is ${change} in change.")
     print(f"Here is your {comand} ☕️. Enjoy!")
     money += monetary
     drop_resources(comand)