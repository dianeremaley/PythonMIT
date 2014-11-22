# Problem Set 1 - Problem 2
# Name: Diane Remaley
# Collaborators: None
# Time Spent 1 hour
#

starting_balance = float(raw_input("Enter the outstanding balance on your credit card: "))
rate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))

# guess at the amount
guess = 0
balance = starting_balance
month = 1

while balance > 0 : 
    balance = starting_balance
    for month in range(1,13) :
        int_paid = round((rate/12)*balance, 2) 
        principal_paid = guess - int_paid
        balance = balance - principal_paid
        if balance <=0 : break
    if balance <=0 : break
    else : guess = guess + 10

print "RESULT"
print "Monthly payment to pay off debt in 1 year: %d" % guess
print "Number of months needed: %d" % month
print "Remaining Balance: $%.2f" % balance


