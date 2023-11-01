# programming_dictionary = {
#   "Bug": "An error in a program that prevents the program from running as expected.", 
#   "Function": "A piece of code that you can easily call over and over again.",
#   "Loop": "The action of doing something over and over again"
# }

# programming_dictionary["Bug"] = "A moss in the computer."

# programming_dictionary["For"] = "An interator"

# #whipe dictionary
# # programming_dictionary = {}

# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }

# #TODO-1: Create an empty dictionary called students_grades
# student_grades = {}

# #TODO-2: Write your code below to add the grades
# for key in student_scores:
#   if student_scores[key] <= 70:
#     student_grades[key] = "Fail"
#   elif student_scores[key] <= 80:
#     student_grades[key] = "Acceptable"
#   elif student_scores[key] <= 90:
#     student_grades[key] = "Exceeds Expectations"
#   else:
#     student_grades[key] = "Outstanding"

# print(student_grades)

##Nesting
# capitals = {
#   "France": "Paris",
#   "Germany": "Berlin",
# }

# travel_log = {
#   "France": {"cities_visited":["Paris","Lille","Dijon"], "total_visits": 12},
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }


# print(travel_log)

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(tara, vizite, orase):
# #   travel_log.append({"country": tara, "visits": vizite, "cities": orase})
#     new_country = {}
#     new_country["country"] = tara
#     new_country["visits"] = vizite
#     new_country["cities"] = orase
#     travel_log.append(new_country)


# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


# import blind_auction_art
# import os

# clear = lambda: os.system('cls')

# participants = []

# def add_participants(nume, licitare):
#   new_participants = {}
#   new_participants[nume] = licitare
#   participants.append(new_participants)


# print(blind_auction_art.logo)
# print("Welcome to the secret auction program.")

# continue_auction = True
# while continue_auction:

#   name_key = input("What is your name?: ")
#   bid_value = input("What's your bid?: ") 

#   add_participants(name_key, bid_value)

#   other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

#   if other_bidders == "yes":
#     clear()
#     continue
#   elif other_bidders == "no":
#     continue_auction = False
#   else:
#     print("Please select only 'yes' or 'no'.")
#     continue

# winner = ''
# money = 0
# for participant in participants:
#  for bidder in participant:
#     value = int(participant[bidder])
#     if value > money:
#       money = value
#       winner = bidder
#       money = value

# print(f"The winner is {winner} with a bid of {money} lei.")