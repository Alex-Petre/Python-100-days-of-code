print("Welcome to the tip calculator")
total_bill = input("What was the total bill? ")
people = input("How many people to split the bill? ")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

calc_billsplit = (float(total_bill) / float (people))
calc_procent = (float(total_bill) * float (percentage)) / 100
calc_split_procent =  (float (calc_procent) / float (people))
calc_total = round(calc_billsplit + calc_split_procent,2)

print(f"Each person should pay: {calc_total} lei")