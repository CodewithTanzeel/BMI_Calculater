# Get user's weight in pounds
weight_pounds = float(input("Enter your weight in pounds: "))

# Convert weight from pounds to kilograms (1 pound = 0.453592 kg)
weight_kg = weight_pounds * 0.453592

# Get user's height in inches
height_inches = float(input("Enter your height in inches: "))

# Convert height from inches to meters (1 inch = 0.0254 meters)
height_meters = height_inches * 0.0254

# Calculate BMI
bmi = weight_kg / (height_meters ** 2)

# Display the result
print(f"Your BMI is: {bmi:.2f}")

# Interpret the result
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
