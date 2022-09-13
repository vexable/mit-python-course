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
# epsilon = 0.01 
# y = 54.0
# guess = y/2.0
# numGuesses = 0
# while abs(guess*guess) >= epsilon:
#     numGuesses += 1
#     guess = guess - (((guess**2)-y)/(2*guess))
# print(numGuesses)
# print(y)
# print(guess)

#function example
# def is_even(i):
#     """
#     Input: i, a positive int
#     Returns True if even, otherwise False
#     """
#     print("Hi")
#     return i%2 == 0

#function with variable scope
# def f (x):
#     x = x+1
#     print("in f(x), x = ", x)
#     return x
# x=3
# z= f(x)
#result is 4

#example of function as parameter/arguement
# def func_a():
#     print("inside func_a")
#     return
# def func_b(y):
#     print("inside func_b")
#     return y
# def func_c(z):
#     print("inside func_c")
#     return z
# print(func_a)
# print(5 + func_b(2))
# print(func_c(func_a))

#name simple function
# def printName(firstName,lastName,reverse):
#     if reverse:
#         print(lastName,firstName)
#     else:
#         print(firstName,lastName)
# printName("Pranesh","Sathish Kumar","False")

# def foo(x, y = 5):
#    def bar(x):
#       return x + 1
#    return bar(y * 2)
          
# foo(3)