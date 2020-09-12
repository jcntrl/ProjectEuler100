'''
Power digit sum
Submit

 Show HTML problem content 
Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
import timeit

def PowerDigitSumA1(n=2, power=1000):
    N = pow(n,power)
    Nstr = str(N)
    Nrarr = [int(i) for i in Nstr]
    Nsum = sum(Nrarr)
    # for i in Nstr:
    #     Nsum += int(i)
    return Nsum

def PowerDigitSumA2(n=2, power=1000):
    N = pow(n,power)
    Nstr = str(N)
    Nsum = 0
    for i in Nstr:
        Nsum += int(i)
    return Nsum

#----------------------------------------------------------------------------
t0 = timeit.default_timer()
r = PowerDigitSumA1()
t1 = timeit.default_timer()
dt = t1-t0
print('----------\nPowerDigitSum by Approach1\n', r, round(dt*1e6), round(dt,1))
# result: 1366, approx 100 mus
#----------------------------------------------------------------------------
t0 = timeit.default_timer()
r = PowerDigitSumA2()
t1 = timeit.default_timer()
dt = t1-t0
print('----------\nPowerDigitSum by Approach2\n', r, round(dt*1e6), round(dt,1))
# result: 1366, approx 70 mus
#----------------------------------------------------------------------------