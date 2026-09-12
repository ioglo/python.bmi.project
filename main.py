from bmi import calculate_bmi, bmi_category

weight = float(input("Enter your weight in kilograms:"))
height = float(input("Enter your height in meters:"))

bmi = calculate_bmi(weight, height)

print(f"BMI = {bmi:.2f}")
category = bmi_category(bmi)
print(f"Category: {category}")