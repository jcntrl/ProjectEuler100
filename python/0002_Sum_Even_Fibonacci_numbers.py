'''Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def fastfibbottomup(n):
    '''
    bottom up iterative dynamic programming solution
    '''
    if n == 0 or n == 1:
        return n
    nmin2, nmin1 = 0, 1     #base case
    for fib in range(n-1):  #draw this out on a bottomup table
        result = nmin2 + nmin1  #recurrence relation
        nmin2, nmin1 = nmin1, result
    return result


def SumEvenFib(fmax):
    n = 0
    fib_n = 0
    res = 0
    while fib_n < fmax:
        fib_n = fastfibbottomup(n)
        if fib_n % 2 == 0:
            res += fib_n
        n += 1
    return res


# test case
assert SumEvenFib(89) == 44, "Should be 44"
# output
print(SumEvenFib(4_000_000))