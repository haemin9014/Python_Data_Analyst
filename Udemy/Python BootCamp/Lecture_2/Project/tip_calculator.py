print("Welcome to the tip calculator.");
total_bill = float(input("What was the total bill? $"));
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "));
tip = tip_percentage /100 * total_bill;
people = int(input("How many people to split the bill? "));
final_cost = (total_bill + tip)/people;
print(f"Each person should pay: ${round(final_cost, 2)}");