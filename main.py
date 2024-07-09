print("Welcome to the tip calculator")
# User adds total cost of bill
bill = float(input("What was the total bill? "))
# User adds desired tip
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
# User adds amount of peoples splitting the bill
people = float(input("How many people to split the bill? "))
# Calculates the total cost of the bill
meal_with_tip = (bill/people) / 100 * percentage + bill/people
# Rounds the total cost of the bill to 2 decimal places
round(meal_with_tip, 2)
# Prints the total cost of the bill to the user
print(f"Each Person should pay: {meal_with_tip}")
