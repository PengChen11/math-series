# function to calculate the nth fibonacci number. I hate using recursion for this task cause the big O is 2*n and when n goes above 30, it eats up all my computer's resources.
# The following solution's big O is only n-2. much faster.
# n starts with 0.
def fibonacci(n):
    prev, nex = 0, 1
    for i in range(n - 1):
        prev, nex = nex, prev + nex
    if n==0:
        return prev
    else:
        return nex

# this is the calculation based on fibonacci's fomular.
# (1+5**0.5)/2 is called golden mean
# I don't know how python calculate floats, but these two method starts to give different  value when n=72. feels like something wrong with acturacy for float calculation when it's really a big number.
# n starts with 0

def fibonacci_1(n):
    return int((((1 + 5 ** 0.5) / 2)**n-(1-((1 + 5 ** 0.5) / 2))**n)/(5**0.5))


# function to calculate the nth lucas number.
# n starts with 0
def lucas(n):
    prev, nex = 2, 1
    for i in range(n - 1):
        prev, nex = nex, prev + nex
    if n==0:
        return prev
    else:
        return nex


# function to calculate the nth number, based on 2 optional prams.
# if no optional prams input, then using fibonacci.
def sum_series(n,prev=0,nex=1):
    for i in range(n - 1):
        prev, nex = nex, prev + nex
    if n==0:
        return prev
    else:
        return nex

