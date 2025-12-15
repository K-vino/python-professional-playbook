W = float(input("Weight in KG: "))
H = float(input("Height in CM: "))

# Convert height from cm to meters
H = H / 100

# Calculate BMI
BMI = W / (H ** 2)

print("BMI Value is", round(BMI, 2))
