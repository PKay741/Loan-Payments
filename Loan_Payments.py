#import pandas as pd

def calculate_monthly_payment():
    # Prompt user for loan details
    loan_amount = float(input("Enter the loan amount (principal) in CAD: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in percentage): "))
    loan_term_years = int(input("Enter the loan term in years: "))

    # Calculate monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12 / 100

    # Calculate total number of payments (months)
    total_payments = loan_term_years * 12

    # Calculate the new price to be paid for taking the loan
    interest_paid = (loan_amount * total_payments * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)
    total_price = loan_amount + interest_paid

    # Calculate monthly payment
    monthly_payment = total_price / total_payments

    # Print results
    print("\nLoan Details:")
    print(f"Loan Amount (Principal): {loan_amount:.2f} CAD")
    print(f"Annual Interest Rate: {annual_interest_rate:.2f}%")
    print(f"Loan Term: {loan_term_years} years\n")

    print("Calculations:")
    print(f"Interest Paid: {interest_paid:.2f} CAD")
    print(f"Total Price (Principal + Interest): {total_price:.2f} CAD")
    print(f"Monthly Payment: {monthly_payment:.2f} CAD")

# Main loop
while True:
    calculate_monthly_payment()
    another_loan = input("\nDo you want to calculate another loan? (yes/no): ").lower()
    if another_loan != "yes":
        break