"""
Purpose : Savings Bank

        Intitial Balance 0

Algorithm

step 1: Create an variable 'balance' with initial value 0
step 2: Initial deposit of min balance 1500
step 3: Salary credited of 3300
step 4: Online purchase of 33.33
step 5: House rent paid of 1500
step 6: Display balance
"""

initial_balance = 0
initial_balance += 1500   # added 1500 as minimum balance
initial_balance += 3300   # salary credited to account
initial_balance -= 33.33  # amount debited due to purchase
initial_balance -= 1500   # paid house rent
print("Final balanace is =" ,initial_balance)
