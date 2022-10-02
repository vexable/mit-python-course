x = "pi"
y = "pie"

x, y = y, x

# print(x)
# print(y)

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    exponent = 0
    while b ** exponent <= x:
        exponent += 1
    exponent -= 1
    return exponent

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    result = 0
    x = 0
    if listA == [0]:
        return 0
    while x < len(listA):
        result = result + (listA[x] * listB[x])
        x += 1
    return result

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # values = list(aDict.values())
    # if target not in values:
    #     return []
    keys = list(aDict.keys())
    s = 0
    x = 0
    for s in range(len(keys)):
        print(s)
        print(keys)
        print(x)
        if aDict.get(keys[x]) != target:
            keys.remove(keys[x])
        else:
            x += 1
            s -= 1
    if len(keys) == 1:
        if aDict.get(keys[0]) != target:
            return []
    keys.sort()
    return keys


def gcd2(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """

    if a > b:
        currentFactor = b
    elif b > a:
        currentFactor = a
    while True:
        if a % currentFactor == 0 and b % currentFactor == 0:
            return currentFactor
        else:
            if a >= b:
                currentFactor -= b
            elif b > a:
                currentFactor -= a
        print(currentFactor) 

def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    if a == 0:
        return b
    if b == 0:
        return a
    if b > a:
        return gcd(a, b % a)
    else:
        return gcd(b, a % b)



def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    copy = L.copy()
    for i in copy:
        if not g(f(i)):
            L.remove(i)
    if L == []:
        globals()['L'] = L
        return -1
    resultMax = L[0]
    for x in L:
        if x > resultMax:
            resultMax = x
    globals()['L'] = L
    return resultMax
def f(i):
    return i * 5
def g(i):
    return i < 5

L = [6,6,6,-1000,6,6,-10000,6,6]
print(applyF_filterG( L, f, g))
print(L)

