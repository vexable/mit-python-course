balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12
minMonthlyPayment = monthlyPaymentRate * balance
previousBalance = balance

unpaidBalance = 0
monthlyInterest = 0

def calc():
    global balance
    global minMonthlyPayment
    global previousBalance
    balance = balance - round(minMonthlyPayment, 2)
    balance = round(balance + (balance * monthlyInterestRate), 2)
    minMonthlyPayment = round(monthlyPaymentRate* previousBalance, 2)
    previousBalance = balance

def calc2():
    global balance
    global minMonthlyPayment
    global previousBalance
    global unpaidBalance
    global monthlyInterest

    minMonthlyPayment = monthlyPaymentRate * previousBalance
    unpaidBalance = previousBalance - minMonthlyPayment
    monthlyInterest = unpaidBalance * monthlyInterestRate

    previousBalance = unpaidBalance + monthlyInterest



    # balance = balance - (minMonthlyPayment, 2)
    # balance = round(balance + (balance * monthlyInterestRate), 2)
    
    # previousBalance = balance

x=0
while x != 12:
    calc2()
    x += 1

print(round(unpaidBalance + monthlyInterest, 2))
    # print(balance)
    # print(minMonthlyPayment)
    # print(previousBalance)
