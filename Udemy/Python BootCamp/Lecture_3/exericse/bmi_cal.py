height = float(input("enter your height in m:\n"));
weight = float(input("enter your weight in kg:\n"));
bmi = round(weight / (height ** 2));

print(f"your height is {height} and your weight is {weight}.\nTherefore, your bmi is {bmi}");
if bmi < 18.5:
    print("Under 18.5 they are underweight");
elif bmi > 18.5 and bmi <= 25:
    print("normal weight");
elif bmi > 25 and bmi <= 30:
    print("overweight");
elif bmi > 30 and bmi <= 35:
    print("obese");
else:
    print("clinically obese")
