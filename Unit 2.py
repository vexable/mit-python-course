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

#converts decimal to binary format
# num = 11
# result = ''
# if num < 0:
#     isNeg = True
#     num = abs(num)
# else:
#     isNeg = False
# while num > 0:
#     result = str(num%2) + result
#     num = num//2 
#print(result)

#newton-raphson algorithm
epsilon = 0.01 
y = 54.0
guess = y/2.0
numGuesses = 0
while abs(guess*guess) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2)-y)/(2*guess))
print(numGuesses)
print(y)
print(guess)