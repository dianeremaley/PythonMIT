# Problem Set 1 - Problem 3
# Name: Diane Remaley
# Collaborators: None
# Time 09:15 - 10:15 
# Keep getting rounding errors and month errors.


# check_if_paid:  Checks if balance will be paid off.  Returns true if guess as a monthly
# payment will result in a zero balance after 12 months. 

# Get User Input
starting_balance = float(raw_input("Enter the outstanding balance on your credit card: "))
rate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
months = 1
balance = starting_balance
# establish upper and lower bounds, initialize variables
lower_bound = round(balance/12.0, 2)
upper_bound = round((balance * (1 + (rate/12.0))**12.0)/12.0, 2)
epsilon = abs(upper_bound - lower_bound)

while epsilon > .01 :  #Keep running until upper bound and lower bound are close
    balance = starting_balance
    guess = (lower_bound+upper_bound)/2.0
    months = 1
    print "Guess: %.2f " % guess
    print "Upper: %.2f " % upper_bound
    print "Lower: %.2f" % lower_bound
    for month in range(1,13) :
        int_paid = round((rate/12)*balance, 2) 
        principal_paid = round(guess, 2) - int_paid
        balance = balance - principal_paid
        if balance <=0 : break
        months += 1
    if balance <=0 : upper_bound = guess
    else : lower_bound = guess
    epsilon = upper_bound - lower_bound
   

print "RESULT"
print "Monthly payment to pay off debt in 1 year: %.2f" % guess
print "Number of months needed %d" % months
print "Remaining Balance: $%.2f" % balance


