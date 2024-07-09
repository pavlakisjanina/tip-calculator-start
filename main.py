print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))
meal_with_tip = (bill/people) / 100 * percentage + bill/people
round(meal_with_tip, 2)
print(f"Each Person should pay: {meal_with_tip}")
