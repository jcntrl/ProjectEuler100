'''
Names scores
Submit

 Show HTML problem content 
Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import csv
import string

#GLOBAL VARS:
ALPHA = string.ascii_uppercase
ALPHADICT = {ALPHA[i]:i+1 for i in range(len(ALPHA))}

def loadfile(filename):
    with open(filename) as rawdata:
        data = csv.reader(rawdata)
        for item in data: # assumes input source data file is a single-line CSV, this won't work if otherwise
            return item

def alphascore(name):
    score = 0
    for ltr in name:
        score += ALPHADICT[ltr]
    return score

def totalscores(data):
    sdata = sorted(data)
    tscore = 0
    for i in range(len(sdata)):
        pscore = i+1 #positional score
        ascore = alphascore(sdata[i]) #alphabetical score
        tscore += pscore * ascore
    return tscore


# data = loadfile('0022_names_test.txt')
data = loadfile('0022_names.txt')
result = totalscores(data)
print(result)