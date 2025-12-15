"""

# Fixed conversion rates (as of example)
conversion_rates = {
    "USD": 80.1,   # 1 USD = 80.1 INR
    "EUR": 88.5,   # 1 EUR = 88.5 INR
    "GBP": 103.2,  # 1 GBP = 103.2 INR
    "JPY": 0.57,   # 1 JPY = 0.57 INR
    "AED": 21.8    # 1 AED = 21.8 INR
}

# Input in INR
inr = float(input("Enter amount in INR: "))

print("\nConverted Amounts:")
for currency, rate in conversion_rates.items():
    converted = inr / rate
    print(f"{currency}: {converted:.3f}")

"""


# Fixed conversion rate (example: 1 USD = 80.1 INR)
conversion_rate = 80.1

# Input amount in INR
inr = float(input("Enter amount in INR: "))

# Convert to USD
usd = inr / conversion_rate

# Print result with 3 decimal places
print(f"Amount in USD: ${usd:.3f}")
