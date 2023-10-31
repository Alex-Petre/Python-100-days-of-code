#==============APP 1 START==========================
# fruits = ["Apple", "Pear", "Peach"]
# for fruit in fruits:
#   print(fruit)
#==============APP 1 END============================

#==============APP 2 START==========================
#Day 5.1 Average Height
# student_heights = input("Input a list of student heights ").split()
# for n in range(0,len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# print(student_heights)

# def lenght_of_list(list):
#   count = 0
#   for i in list:
#     count += 1
#   return count

# def sum_of_items_in_list(list):
#   temp = 0
#   for i in list:
#     temp += i
#   return temp


# calculate_average_height = round(sum_of_items_in_list(student_heights) / lenght_of_list(student_heights))
# print(f"The average height of your students is {calculate_average_height}")

#==============APP 2 END==========================


#==============APP 3 START==========================
#Day 5.2 Highest Score

# student_scores = input("Input a list of student scores ").split()
# for n in range(0,len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)


# def max_scores(list):
#   max_value = 0
#   for i in list:
#     if i > max_value:
#       max_value = i
#   return max_value

# print(f"The highest score in the class is: {max_scores(student_scores)}")

#==============APP 3 END==========================


#==============APP 4 START==========================
#Day 5.3 Adding Evens Exercise
# totalSum = 0
# for nr in range(2, 101, 2):
#   totalSum += nr
# print(totalSum)

#==============APP 4 END==========================


#==============APP 5 START==========================
#Day 5.4 FizzBuzz

# for nr in range(1,101):
#     if nr % 3 == 0 and nr % 5 == 0:
#       print("FizzBuzz")
#     elif nr % 3 == 0:
#       print("Fizz")
#     elif nr % 5 == 0:
#       print("Buzz")
#     else:
#       print(nr)
#==============APP 5 END==========================


#==============APP 6 START==========================
#Day 5.5 Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

#==============APP 6 END==========================