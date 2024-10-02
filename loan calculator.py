"""
Student Name: Hannes Meyer-Rahlfs   
Program Title: Hipster's Local Vinyl Records   
"""

# Input loan details
A = float(input("Enter the loan amount: "))
r = float(input("Enter the annual interest rate: "))
n = float(input("Enter the loan term in years: "))

# Calculate weekly interest rate (i)
i = r / 5200

# Calculate denominator part of the formula
Denominator = 1 - (1 + i) ** (-52 * n)

# Calculate the weekly payment
Weekly_Payment = (i / Denominator) * A

# Output the result
print(f"The weekly payment is: ${Weekly_Payment:.2f}")