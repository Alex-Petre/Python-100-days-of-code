# def form_nume(nume):
#   newf_name = ''
#   for i in range(len(nume)):
#     if i == 0:
#       newf_name += nume[i].capitalize()
#     else:
#       newf_name += nume[i].lower()
#   return newf_name

# def format_name(f_name, l_name):
#   newf_name = form_nume(f_name)
#   newl_name = form_nume(l_name)
#   return newf_name +" "+ newl_name

  
# fnume = input("First Name ")
# lnume = input("Last Name ")

# print(format_name(fnume, lnume))

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#   if month > 12 or month < 1:
#     return "Invalid month"
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
#   index_of_month = month -1
#   if is_leap(year):
#     month_days[1] = 29
#     return month_days[index_of_month]
#   else:
#     return month_days[index_of_month]

  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

from calculator_art import logo

def inmultire(nr1, nr2):
   result = nr1 * nr2
   return result

def impartire(nr1, nr2):
   result = nr1 / nr2
   return result

def adunare(nr1, nr2):
   result = nr1 + nr2
   return result

def scadere(nr1, nr2):
   result = nr1 - nr2
   return result

operations = {
   "+": adunare,
   "-": scadere,
   "*": inmultire,
   "/": impartire,
}
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    pick_operation = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    operation_symbol = operations[pick_operation]
    answer = operation_symbol(num1, num2)

    print(f"{num1} {pick_operation} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()


calculator()