# Home Loan EMI Calculator (India)

import math

def ask_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Re-enter.")

def confirm(value, label):
    while True:
        c = input(f"{label} = {value}. Continue? (y/n): ").strip().lower()
        if c == "y":
            return value
        elif c == "n":
            return None
        else:
            print("Enter y or n.")

# Loan amount in lakhs
while True:
    amt_lakhs = ask_float("Enter loan amount (in lakhs): ")
    if confirm(amt_lakhs, "Loan amount (lakhs)") is not None:
        break

# Interest rate
while True:
    rate = ask_float("Enter annual interest rate (%): ")
    if confirm(rate, "Interest rate (%)") is not None:
        break

# Tenure years
while True:
    years = ask_float("Enter tenure years: ")
    if confirm(years, "Tenure years") is not None:
        break

# Tenure months
while True:
    months = ask_float("Enter additional months: ")
    if confirm(months, "Additional months") is not None:
        break

principal = amt_lakhs * 100000  # lakhs to INR
monthly_rate = rate / (12 * 100)
total_months = int(years * 12 + months)

emi = (principal * monthly_rate * math.pow(1 + monthly_rate, total_months)) / \
      (math.pow(1 + monthly_rate, total_months) - 1)

total_payment = emi * total_months

print("\nRESULT")
print(f"Monthly EMI: ₹{emi:,.2f}")
print(f"Total amount paid: ₹{total_payment:,.2f}")
print(f"Total interest paid: ₹{(total_payment - principal):,.2f}")

