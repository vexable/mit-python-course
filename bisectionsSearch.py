balance = 320000
annualInterestRate = 0.2
previousBalance = balance
monthlyInterestRate = annualInterestRate/12
monthlyLower = balance/12
monthlyUpper = 1000000
guess = round((monthlyLower+monthlyUpper)/2,2)
monthlyUnpaid = balance - guess
monthlyInterest = monthlyUnpaid * monthlyInterestRate

balance = previousBalance
iter = 0
epsilon = 0.1
balance2 = balance
while True:
    balance = previousBalance
    iter = 0
    while iter != 12:
        monthlyUnpaid = balance-guess
        monthlyInterest = monthlyUnpaid * monthlyInterestRate
        balance = monthlyUnpaid + monthlyInterest
        iter = iter + 1
    balance = round(balance,2)
    if balance != epsilon:
        if balance > epsilon:
            monthlyLower = guess
            guess = round((monthlyLower+monthlyUpper)/2,2)
        if balance < 0:
            monthlyUpper = guess
            guess = round((monthlyLower+monthlyUpper)/2,2)
    elif balance <= epsilon and not balance < 0:
        break
    if balance2 == balance:
        break
    balance2 = balance
print("Lowest Payment: " + str(guess))
