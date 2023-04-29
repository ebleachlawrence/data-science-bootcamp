# This program contains two financial calculators, an investment calculator and a home loan repayment calculator

import math

# Displays options and takes user input

user_input = input("""We have two types of calculators:
Investment - to calculate the amount of interest you'll earn on your investment
Bond - to calculate the amount you'll have to pay on a home loan
Enter either 'investment' or 'bond' from the menu above to proceed: """)

# Calculates simple and compound investments

if user_input.lower() == 'investment':
    initial_deposit = float(input("How much are you depositing? "))
    interest_rate = input("What is your interest rate? ").strip("%")
    interest_rate = float(interest_rate)/100
    years_investing = int(input("How many years will you be investing? "))
    interest = input("Do you want simple or compound interest? ")

    if interest.lower() == 'simple':
        total_amount = initial_deposit*(1 + interest_rate*years_investing)
        total_amount = round(total_amount,2)
        print("Your total including interest will be £" + str(total_amount))
    elif interest.lower() == 'compound':
        total_amount = initial_deposit * math.pow((1+interest_rate), years_investing)
        total_amount_rounded = round(total_amount,2)
        print("Your total amount, including interest will be £" + str(total_amount_rounded))
    else:
        print("Sorry you didn't enter either 'simple' or 'compound'. Please start again.")

# Calculates monthly repayments on bonds

elif user_input.lower() == 'bond':
    house_value = float(input("What is the present value of the house? "))
    interest_rate = input("What is your interest rate? ").strip("%")
    interest_rate = (float(interest_rate)/100)/12
    repayment_months = int(input("How many months will it take to repay the bond? "))
    repayment = (interest_rate * house_value)/((1- + interest_rate) ** (-repayment_months))
    repayment_rounded = round(repayment,2)
    print("Each month you will have to repay £" + str(repayment_rounded)) 

# Gives error message when incorrect input is recieved. Not sure how to make the program start again yet

else:
    print("Sorry you didn't enter either 'investment' or 'bond. Please start again.")