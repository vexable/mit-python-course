# x = 25
# epsilon = 0.01
# step = 0.1
# guess = 0.0

# while guess <= x:
#     if abs(guess**2 -x) < epsilon:
#         break
#     else:
#         guess += step

# if abs(guess**2 - x) >= epsilon:
#     print('failed')
# else:
#     print('succeeded: ' + str(guess))
# quit



# x= 27
# epsilon = 0.01
# high = x
# low = 1.00
# num_guesses = 0
# guess = (high + low)/2.0
# while abs(guess **3 - x) >= epsilon:
#     num_guesses += 1
#     if guess**3 < x:
#         low = guess 
#     else:
#         high = guess
#     guess = (high + low)/2.0
# print(guess)
# print(num_guesses)

#The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
# The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!