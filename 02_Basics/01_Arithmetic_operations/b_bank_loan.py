"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

             A = Final Amount
             P = Initial Principal balance
             r = annual interest rate
             t = time(in years)

    Compound Interest calculation
             A = P (1 + r/n) ^ (n * t)

"""

# Simple Interest

principal_amount = float(input("Enter amount :"))
interest_rate = float(input("Enter interest rate :"))
time_years = float(input("Enter num of years:"))

final_amount = principal_amount * (1 + interest_rate * time_years)

print("Simple Interest is= " ,final_amount)

# Compound interest 

n = float(input("enter num of times interest compounds per year :"))
compound_interest = principal_amount * (1 + interest_rate / n) ** (n * time_years)

print("Compound interest is= ", compound_interest)