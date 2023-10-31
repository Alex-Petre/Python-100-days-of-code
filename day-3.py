# #=======APP 1 Start=================================
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age?  "))
#   ticket = 0
#   if age < 12:
#     print("5$")
#     ticket = 5
#   elif age <= 18:
#     print("7$")
#     ticket = 7
#   else:
#     ticket = 12
#     print("12$")
#   photo = input("Do you want photos? ")
#   if photo == "yes":
#     ticket += 3
#     print(f"The total bill is {ticket}$")
#   elif photo == "no":
#     ticket
#     print(f"The total bill is {ticket}$")
# else:
#   print("Sorry, you have to grow taller before you can ride.")
# #=======APP 1 End====================================

#=======APP 2 Start=================================
# number = int(input("Which number do you want to check  "))

# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

#=======APP 2 End=================================


#=======APP 3 Start=================================
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = round(weight / height ** 2)

# if bmi < 18.5:
#   print(f"Your bmi is {bmi}, your are underweight.")
# elif bmi < 25:
#   print(f"Your bmi is {bmi}, you have normal weight")
# elif bmi < 30:
#   print(f"Your bmi is {bmi}, you are overweight")
# elif bmi < 35:
#   print(f"Your bmi is {bmi}, you are obese")
# else:
#   print(f"Your bmi is {bmi}, you are clinically obese")

#=======APP 3 End=================================

#=======APP 4 Start=================================
# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print(f"The {year}, is LEAP year")
#     else:
#       print(f"The {year}, is  NOT a LEAP year")  
#   else:
#     print(f"The {year}, is a LEAP year")    
# else:
#   print(f"The {year}, is  NOT a LEAP year")
 
#=======APP 4 End=================================


#=======APP 5 Start=================================
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# pizza_price = 0

# if size == "S":
#   pizza_price = 15
#   if add_pepperoni == "Y":
#     pizza_price += 2
#   else:
#     pizza_price
# elif size == "M":
#   pizza_price = 20
#   if add_pepperoni == "Y":
#     pizza_price += 3
#   else:
#     pizza_price
# elif size == "L":
#   pizza_price = 25
#   if add_pepperoni == "Y":
#     pizza_price += 3
#   else:
#     pizza_price
# if extra_cheese == "Y":
#   pizza_price += 1
# else:
#   pizza_price
# print(f"Your final bill is: {pizza_price}$.")

#=======APP 5 End=================================


#=======APP 6 Start=================================
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# combined_string = name1 + name2
# lower_case_string = combined_string.lower()

# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")

# true = t + r + u + e


# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")

# love = l + o + v + e


# love_score = int(str(true) + str(love))

# if love_score < 10 or love_score > 90:
#   print(f"Your love score is {love_score}, you go together like coke and mentos.")
# elif (love_score >= 40) and (love_score <= 50):
#   print(f"Your score is {love_score}, you are alright together.")
# else:
#   print(f"Your score is {love_score}")

#=======APP 6 End=================================


#=======APP 7 Start=================================
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island. \nYour mission is to find the treasure.")
print("You find yourself on a remote island, standing in front of an old, mysterious door. The door has three different colored locks: a red lock, a blue lock, and a green lock. You remember a legend about a hidden treasure on this island, but to find it, you must make the right choices.")

choice = input("1.Turn left and explore the jungle. \n2.Turn right and venture into a dark cave.\n")

if choice.lower() == "left":
  choice = input("You decide to turn left and explore the dense jungle. After hours of wandering, you find yourself lost and without supplies. Eventually, you find a river that you have to cross. \nDo you wait for the boat or swim across the river?\n")
  if choice.lower() == "swim":
    print('''
****************************************************      
                       -"""-.
                     /       \ 
                    ;_.-"""-._;
 .,_       __,.---.-(=(o)-(o)=)-.---.,__       _,.
 '._'--"```          \   ^   /          ```"--'_.'
    ``"''~---~~%^%^.%.`._0_.'%,^%^%^~~---~''"``
    ~^~- `^-% ^~.%~%.^~-%-~.%-^.% ~`% ~-`%^`-~^~
       ~^- ~^- `~.^- %`~.%~-'%~^- %~^- ~^
*************************************************** 
''')
    print('''
    **************************************************************       
            __________           __________           __________ 
           |  __  __  |         |  __  __  |         |  __  __  |
           | |  ||  | |         | |  ||  | |         | |  ||  | |
           | |  ||  | |         | |  ||  | |         | |  ||  | |
           | |__||__| |         | |__||__| |         | |__||__| |
           |  __  __()|         |  __  __()|         |  __  __()|
           | |  ||  | |         | |  ||  | |         | |  ||  | |
           | |  ||  | |         | |  ||  | |         | |  ||  | |
           | |  ||  | |         | |  ||  | |         | |  ||  | |
           | |  ||  | |         | |  ||  | |         | |  ||  | |
           | |__||__| |         | |__||__| |         | |__||__| |
           |__________|         |__________|         |__________|
    **************************************************************
    ''')
    choice = input('You choose to swim across the river to the other side. As you reach the opposite shore, you notice three doors in front of you, each with a different color: red, blue, and green. You also spot a message carved into a rock that reads, "Choose wisely."')
    if choice.lower() == "red":
      print("You decide to open the red door. \nInside the red door, you find a dead-end room. Game over.")
    elif choice.lower() == "blue":
      print("You decide to open the blue door. \nInside the blue door, you find a dead-end room. Game over.")
    elif choice.lower() == "green":
      print("You opt for the green door. Inside the green door, you uncover the legendary treasure! Congratulations, you've found the hidden treasure and won the game!")
  elif choice.lower() == "wait":
    print("A tribe of indigens came from the jungle and killed you. GAME OVER!")
elif choice.lower() == "right":
  print("You turn right and enter the dark cave. As you venture deeper, you encounter a swarm of bats that attack you, and you are unable to escape their onslaught. GAME OVER!")

#=======APP 7 End=================================