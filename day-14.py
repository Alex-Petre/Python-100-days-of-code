from day_14_game_data import data
from day_14_game_art import logo, vs
import os
import random

def random_data():
  return random.choice(data)

def higher_lower():
  compare_A = random_data()
  compare_B = random_data()

  while compare_A == compare_B:
    compare_B = random_data()
  


  continue_playing = True
  score = 0
  while continue_playing != False:
    value_A = compare_A["follower_count"]
    value_B = compare_B["follower_count"]
    print(logo)
    if score != 0:
      print(f"You're right! Current score: {score}")
    print(f"Compare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}.")
    print(vs)
    print(f"Compare B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}.")
    user_chose = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_chose == "a" and value_A > value_B or user_chose == "b" and value_B > value_A:
      score += 1
      compare_A = compare_B
      compare_B = random_data()
      os.system('cls')
    else:
      os.system('cls')
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      continue_playing = False

higher_lower()