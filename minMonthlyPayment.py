


balance = 4331
annualInterestRate = 0.15

monthlyInterestRate = annualInterestRate/12

minimumFixedPay = 0
previousBalance = balance

def min(x):
    global balance
    balance = previousBalance
    global monthlyInterestRate
    global minimumFixedPay
    # monthlyInterest = monthlyUnpaid * monthlyInterestRate
    # print("minimumFixedPay = " + str(minimumFixedPay))
    while x != 12:
        monthlyUnpaid = balance - minimumFixedPay
        monthlyInterest = monthlyUnpaid * monthlyInterestRate
        balance = balance - minimumFixedPay + monthlyInterest
        # print("x=" + str(x) + " previousBalance=" + str(previousBalance))
        x = x + 1

# while previousBalance != 0:
while balance > 0:
    minimumFixedPay += 10
    min(0)
    # print("iteration=" + str(iteration) + " previousBalance=" +str(previousBalance))
    # brea

print("Lowest Payment: " + str(minimumFixedPay))


