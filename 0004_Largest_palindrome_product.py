'''
Largest palindrome product

Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_Palindrome(p):
    '''
    Input: integer.
    Method: converts input to string, reverses and compares.
    Output: returns Boolean.
    '''
    # non-optimized solution
    p, d = str(p), ''
    for i in range(len(p)-1, -1, -1):
        d += p[i]
    
    return p == d
        


def multiply_ndigitnumbers(n):
    '''
    Input: integer number of digit number to multiply.
    Method: 2 nested for loops O(n^2); tests if result is palindrome on each iteration and stores winner vs incumbent.
        Note: should be optimized with dynamic programming if larger results are desired but this is fast enough (< 1s for n=3: up to one minute of computation allowed) for now.
    Output: returns integer result which is the maximum palindrome.
    '''
    rng = range(10 ** (n-1), 10 ** n)
    result = 0
    for x in rng:
        for y in rng:
            tmpresult = x * y
            if is_Palindrome(tmpresult) and tmpresult > result:
                result = tmpresult
    return result


# test cases
assert is_Palindrome(89298)==True, "should be True"
assert is_Palindrome(89297)==False, "should be False"
assert multiply_ndigitnumbers(2)==9009, "should be 9009"

# (Just Do It) ** TM
print(multiply_ndigitnumbers(3))