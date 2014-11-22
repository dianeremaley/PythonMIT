# Problem Set 1
# Name: Diane Remaley
# Collaborators: None
# Time Spent : 30 minutes
#

starting_balance = float(raw_input("Enter the outstanding balance on your credit card: "))
rate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
min_payment_rate = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))
balance = round(starting_balance, 2)
total_paid = 0

for month in range (1, 13) :
    min_payment =  round(min_payment_rate * balance, 2)
    int_paid = round(rate/12*balance, 2)
    principal_paid = min_payment - int_paid
    balance = balance - principal_paid
    total_paid = total_paid + int_paid + principal_paid
    print "Month: %s" % month
    print "Minimum Monthly Payment: $%.2f" % min_payment
    print "Principal Paid: $%.2f" % principal_paid
    print "Remaining Balance: $%.2f" % balance
print "RESULT"
print "Total Amount Paid: $%.2f" % total_paid
print "Remaining Balance: $%.2f" % balance


