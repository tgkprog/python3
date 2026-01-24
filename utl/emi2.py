
# Home Loan EMI Calculator (India)
# - Indian comma format (lakhs/crores)
# - Number to words (Indian system)
# - Prints numbers + words

import math

def indian_format(n):
    n = int(round(n))
    s = str(n)
    if len(s) <= 3:
        return s
    last3 = s[-3:]
    rest = s[:-3]
    parts = []
    while len(rest) > 2:
        parts.insert(0, rest[-2:])
        rest = rest[:-2]
    if rest:
        parts.insert(0, rest)
    return ",".join(parts) + "," + last3

def num_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six",
            "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    def two_digits(x):
        if x < 20:
            return ones[x]
        return tens[x // 10] + (" " + ones[x % 10] if x % 10 else "")

    def three_digits(x):
        if x < 100:
            return two_digits(x)
        return ones[x // 100] + " hundred" + (
            " " + two_digits(x % 100) if x % 100 else ""
        )

    if n == 0:
        return "zero"

    parts = []
    crore = n // 10000000
    n %= 10000000
    lakh = n // 100000
    n %= 100000
    thousand = n // 1000
    n %= 1000

    if crore:
        parts.append(three_digits(crore) + " crore")
    if lakh:
        parts.append(three_digits(lakh) + " lakh")
    if thousand:
        parts.append(three_digits(thousand) + " thousand")
    if n:
        parts.append(three_digits(n))

    return " ".join(parts)

def ask_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Invalid number. Re-enter.")

def confirm(val, label):
    while True:
        c = input(f"{label} = {val}. Continue? (y/n): ").lower()
        if c == "y":
            return True
        if c == "n":
            return False

# Input flow
while True:
    loan_lakhs = ask_float("Enter loan amount (in lakhs): ")
    if confirm(loan_lakhs, "Loan amount (lakhs)"):
        break

while True:
    rate = ask_float("Enter annual interest rate (%): ")
    if confirm(rate, "Interest rate (%)"):
        break

while True:
    years = ask_float("Enter tenure years: ")
    if confirm(years, "Tenure years"):
        break

while True:
    months = ask_float("Enter additional months: ")
    if confirm(months, "Additional months"):
        break

principal = loan_lakhs * 100000
monthly_rate = rate / (12 * 100)
total_months = int(years * 12 + months)

emi = (principal * monthly_rate * (1 + monthly_rate) ** total_months) / \
      ((1 + monthly_rate) ** total_months - 1)

total_paid = emi * total_months
interest = total_paid - principal

print("\nRESULT")
print(f"EMI: ₹{indian_format(emi)}")
print(f"  ({num_to_words(int(emi))} rupees)")
print(f"Total Paid: ₹{indian_format(total_paid)}")
print(f"  ({num_to_words(int(total_paid))} rupees)")
print(f"Total Interest: ₹{indian_format(interest)}")
print(f"  ({num_to_words(int(interest))} rupees)")

