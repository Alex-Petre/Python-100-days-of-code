##==========APP 1 Start=======================================
#import random

# coin = random.randint(0,1)
# if(coin == 1):
#   print("Heads")
# else:
#   print("Tails")

##==========APP 1 End=======================================

##==========APP 2 Start=======================================
# import random

# names_of_string = input("Give me everybody's names, separated by a comma.\n")
# names = names_of_string.split(", ")

# print(f"{names[random.randint(0, len(names) -1)]} is going to buy the meal today!")
##==========APP 2 End=======================================


##==========APP 3 Start=======================================
#4.3 Treasure Map
# row1 = ["⬜", "⬜", "⬜"]
# row2 = ["⬜", "⬜", "⬜"]
# row3 = ["⬜", "⬜", "⬜"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# col = int(position[1])
# row = int(position[0])

# map[col-1][row-1] = ' X' 
# print("Treasure Map")
# print(f"{row1}\n{row2}\n{row3}")


##==========APP 3 End=======================================

##==========APP 4 Start=======================================
#4.7 Rock, Paper, Scissors.
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
---'    ____)____
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

def rock_paper_scissors(choice):
  if choice == 0:
    print("ROCK")
    print(rock)
  elif choice == 1:
    print("PAPER")
    print(paper)
  elif choice == 2:
    print("SCISSORS")
    print(scissors)
  else:
    print("ERROR!!! Please select one type")
    player_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    rock_paper_scissors(player_choice)
    pc_choice = computer_choice()
    rock_paper_scissors(pc_choice)
    referee(player_choice, pc_choice)

def referee(player_choice, pc_choice):
  if player_choice == pc_choice:
    print("Draw")
    player_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    rock_paper_scissors(player_choice)
    pc_choice = computer_choice()
    rock_paper_scissors(pc_choice)
    referee(player_choice, pc_choice)
  elif player_choice == 0 and pc_choice == 2:
    print("Rock wins against scissors. You Win")
  elif player_choice == 2 and pc_choice == 1:
    print("Scissors win against paper. You Win")
  elif player_choice == 1 and pc_choice == 0:
    print("Paper wins against rock. You Win")
  elif pc_choice == 0 and player_choice == 2:
    print("Rock wins against scissors. You Lose")
  elif pc_choice == 2 and player_choice == 1:
    print("Scissors win against paper. You Lose")
  elif pc_choice == 1 and player_choice == 0:
    print("Paper wins against rock. You Lose")

def computer_choice():
  print("Computer choice: ")
  pc_choice = random.randint(0,2)
  return pc_choice

print("********************Game of Rock, Paper, Scissors**********************")

player_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
rock_paper_scissors(player_choice)

pc_choice = computer_choice()
rock_paper_scissors(pc_choice)

referee(player_choice, pc_choice)

##==========APP 4 End=======================================