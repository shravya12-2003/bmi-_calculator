# Ask user for weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display BMI and category
print(f"Your BMI is {bmi:.2f}.", end=" ")

# Determine BMI category
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You are in the normal weight range.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are in the obese weight range.")
