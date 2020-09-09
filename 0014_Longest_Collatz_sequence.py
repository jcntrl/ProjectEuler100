'''
Longest Collatz sequence

Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import timeit

def CollatzBruteForce(n, sequence= None):
    if sequence == None:
        sequence = []
    sequence.append(n)
    if n == 0 or n == 1: #basecase
        return sequence
    elif n % 2 == 0: #if even
        n = n // 2
    else: #n must be odd
        n = 3 * n + 1
    
    CollatzBruteForce(n, sequence)
    return sequence


def LongestChainBruteForce(StartNum=0, MaxStartNum = 13): #should return 20 as StartNum=0, MaxStartNum = 13
    LongestChainFound = 0
    while StartNum < MaxStartNum:
        StartNum += 1
        ln = len(CollatzBruteForce(StartNum))
        if ln > LongestChainFound:
            LongestChainFound, WinningStartNum = ln, StartNum
    return LongestChainFound, WinningStartNum


def LongestChainSequenceMemo(maxnum=13, memo={}): #memo = { 1:[1], 2:[2,1], ... n:[sequence] }
    def collatzMemo(n, memo={}):
        if n in memo:
            return memo[n]
        else:
            if n == 0 or n == 1:
                memo[n] = [n]
            elif n % 2 == 0:
                memo[n] = [n] + collatzMemo(n//2, memo)
            else:
                memo[n] = [n] + collatzMemo(3*n+1, memo)
        return memo[n]

    LCF, wsn = [], 1
    for i in range(1, maxnum):
        if i in memo:
            snseq = memo[i]
        else:
            snseq = collatzMemo(i, memo)
        if len(snseq) > len(LCF):
            LCF, wsn = snseq, i
    return len(LCF), wsn 


def LongestChainLengthMemo(maxnum=13, memo={}): #memo = { 1:1, 2:2, 3:8, ..., n:lenofseq }
    def collatzMemo(n, memo={}):
        if n in memo:
            return memo[n]
        if n == 0 or n == 1:
            memo[n] = n
        elif n % 2 == 0:
            memo[n] = collatzMemo(n//2, memo) + 1
        else:
            memo[n] = collatzMemo(3*n+1, memo) + 1
        return memo[n]

    LCF, wcf = 0, 1
    for i in range(1, maxnum):
        if i in memo:
            snlen = memo[i]
        else:
            snlen = collatzMemo(i, memo)
            memo[i] = snlen
        if snlen > LCF:
            LCF, wsn = snlen, i
    return LCF, wsn 


# #---------------------------------------------------------------------------- 
# #----------------------------------------------------------------------------
# n=13
# n=10_000
# n=100_000
n=1_000_000
# #----------------------------------------------------------------------------
t0 = timeit.default_timer()
x = LongestChainBruteForce(MaxStartNum=n)
t1 = timeit.default_timer()
dt = t1-t0
print('----------\nLongest Chain by Brute Force:\n', x, round(dt*100e6), round(dt,1))
    # result (n=13 --> 20): 4239, 5942, 4233, 4354, 4263
    # min --> 4233
    # result (n=1_000_000 --> 525): 45.9, 46.2, 45.8
    # min --> 45.8
# #----------------------------------------------------------------------------
t0 = timeit.default_timer()
x = LongestChainSequenceMemo(n)
t1 = timeit.default_timer()
dt = t1-t0
print('----------\nLongest Chain by Memoized Chain Sequence\n', x, round(dt*100e6), round(dt,1))
    # result (n=13 --> 20): 2586, 2936, 2519, 2347, 2568
    # min --> 2347
    # result (n=1_000_000 --> 525): 16.4, 16.3, 16.2
    # min --> 16.2
# #----------------------------------------------------------------------------
t0 = timeit.default_timer()
x = LongestChainLengthMemo(n)
t1 = timeit.default_timer()
dt = t1-t0
print('----------\nLongest Chain by Memoized Chain Length\n', x, round(dt*100e6), round(dt,1))
    # result (n=13 --> 20): 1655, 2056, 1592, 2037, 1624
    # min --> 1592
    # result (n=1_000_000 --> 525): 1.5, 1.5, 1.5
    # min --> 1.5
# #----------------------------------------------------------------------------