'''
Number letter counts
Submit

 Show HTML problem content 
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''
import timeit, math

basesandspecials = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    1000: "one-thousand"
}


def synth(n, dictionary=basesandspecials):
    ### helper functions ###
    def getintlength(integer):
        integer = abs(integer)
        intlen = 0
        while integer >= 10**intlen:
            intlen += 1
        return intlen

    def breakdown(n):
        # for example, n=368 --> [300, 60, 8]
        # side effect, n=112 --> [100, 10, 2] MUST BE HANDLED SPECIALLY
        intlen = getintlength(n)
        nbreakdown = []
        for order in range(intlen-1, -1, -1):
            tmp = math.floor(n/10**order)
            nbreakdown.append(tmp*10**order)
            n -= tmp*10**order
        return nbreakdown

    def wordify(n, dictionary=basesandspecials):
        # to be called when word was not in memo
        nbreakdown = breakdown(n)
        res = []
        rlen = len(nbreakdown)

        for i in range(rlen):
            if nbreakdown[i] > 0:
                if nbreakdown[i] % 100 == 0: #handle the hundreds-prefix
                    res.append(dictionary[nbreakdown[i]//100])
                    res.append('-hundred')
                    if nbreakdown[i+1] != 0 or nbreakdown[i+2]!= 0:
                        res.append(' and ')
                elif i < rlen-1 and nbreakdown[i] + nbreakdown[i+1] in range(11,20):
                    res.append(dictionary[nbreakdown[i]+nbreakdown[i+1]])
                    break #because this is one of the "special cases" that break the rules AKA TEENS ;)
                elif nbreakdown[i] % 10 == 0: #handles the 'tens'
                    res.append(dictionary[nbreakdown[i]])
                    res.append('-')
                elif nbreakdown[i] in range(1,10):
                    res.append(dictionary[nbreakdown[i]])
        return ''.join(res)
    
    ### main function ###
    if n in dictionary:
        result = dictionary[n]
    else:
        result = wordify(n)
    return result




def lengthOfFirstNWordifiedNumbers(n):
    def wordlen(word):
        wordlen = 0
        for char in word:
            if char not in ['-', ' ']:
                wordlen += 1
        return wordlen
    result = 0
    for i in range(1, n+1):
        result += wordlen(synth(i))

    return result


print(lengthOfFirstNWordifiedNumbers(5)) #should equal 19
print(lengthOfFirstNWordifiedNumbers(1000))