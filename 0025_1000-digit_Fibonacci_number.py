'''
1000-digit Fibonacci number
Submit

 Show HTML problem content 
Problem 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

def fibmdigits(m): #m == num of digits
    memo = {0:0, 1:1}
    def fibfast(n, memo): #verified working
        if n not in memo:
            memo[n] = fibfast(n-2, memo) + fibfast(n-1, memo)
        return memo[n]
    fnum = 0
    flen = 1
    while flen < 10**(m-1) + 1:
        fnum += 1
        flen = fibfast(fnum, memo)
    return flen, fnum
        
        
# ~~~ DRIVER CODE TO EXECUTE ~~~ #


m = 2 # ==> 7th fib num TRUE
m = 3 # ==> 12th fib num TRUE
desiredlen = 1000 # ==> 4782, SOLUTION ___ACCEPTED

result = fibmdigits(desiredlen)
print(
    "\n length of nth fib num:", len(str(result[0])),
    "\n fibonacci index num:", result[1],
    "\n fibonacci number:", result[0]
)

# VERIFY RESULT:

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


print("check: length of result-1th num:", len(str(fastfibbottomup(result[1]-1))))