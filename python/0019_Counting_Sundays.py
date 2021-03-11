'''
Counting Sundays
Submit

 Show HTML problem content 
Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

def isleapyear(year):
    #conditions:
    yrmod4 = year%4 == 0
    yrmod100 = year%100 == 0
    yrmod400 = year%400 == 0
    #tests
    if yrmod4:
        if yrmod100 and yrmod400:
            return True
        elif yrmod100 and not yrmod400:
            return False
        else:
            return True
    else:
        return False


def monthdays(monthno, year):
    thirtyonedays = [1,3,5,7,8,10,12]
    thirtydays = [4,6,9,11]
    if monthno in thirtyonedays:
        return 31
    elif monthno in thirtydays:
        return 30
    else:
        if isleapyear(year):
            return 29
        else:
            return 28


def SundaysOnFirst(startyear, endyear, inityear=1900):
    '''
    using convention that Monday is the first day of week: Mo=1, Tu=2, ... 
    '''
    dayname = 1
    result = 0
    for year in range(inityear, endyear+1):
        for month in range(1,13):
            daysinmonth = monthdays(month, year)
            for daynum in range(1, daysinmonth+1):
                if dayname == 8:
                    dayname = 1
                if dayname == 7 and daynum == 1 and year >= startyear:
                    result += 1
                dayname += 1
    return result



print(SundaysOnFirst(1901, 2000))