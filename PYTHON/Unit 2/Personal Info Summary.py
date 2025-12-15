# Constants (by convention - all caps)
COUNTRY = "India"

# Collecting user input
name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height in cm: ")

# Dynamic Typing - converting age and height to numbers
age = int(age)
height = float(height)

# Introducing a new variable for height in meters
height_m = height / 100  # cm to meters

# Display output
print("\n===== Personal Info Summary =====")
print(f"Name: {name}")
print(f"Age: {age} years")
print(f"Height: {height_m} meters")
print(f"Country: {COUNTRY}")

# Reassign variable dynamically
print("\n🔄 Demonstrating dynamic typing...")
info = age
print(f"Info (int): {info}")

info = name
print(f"Info (string): {info}")

info = height_m
print(f"Info (float): {info}")
