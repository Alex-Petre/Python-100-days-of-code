################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#############NOT BEST PRACTICE#####################
enemies = 1

def increase_enemies():
  global enemies
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
#############NOT BEST PRACTICE#####################
enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()

print(f"enemies outside function: {enemies}")

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from guess_number_art import logo
import random

EASY = 10
HARD = 5

def generate_random_number():
  nr = random.randint(1,100)
  return nr

def check_guess(number, guess):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > number:
    print("Too high.")
    print("Guess again.")
    return attempts - 1
  elif guess < number:
    print("Too low.")
    print("Guess again.")
    return attempts - 1
  else:
    print(f"You got it! The answer was {number}.")
    return "win"

number = generate_random_number()
attempts = 0

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

choose_dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if choose_dificulty == "easy":
  attempts = EASY
else:
  attempts = HARD


continue_play = True
while continue_play:
  if attempts == 0:
    print("You've run out of guesses, you lose.")
    continue_play = False
  elif attempts == "win":
    continue_play = False
  else:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts = check_guess(number, guess)

