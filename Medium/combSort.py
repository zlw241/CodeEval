import random
import math


def comb(items):
    sep = int(len(items)/1.25)
    total = 0
    while sep >= 1:
        first = 0
        second=first+sep
        while second < len(items):
            if items[first] > items[second]:
                items[first],items[second] = items[second], items[first]
            first += 1
            second += 1
        sep = int(sep/1.25)
        total+=1
    return total


test = [3,1,2]
test2 = [5,4,3,2,1] 
test3 = [10,9,8,7,6,5,4,3,2,1]
print(comb(test))
print(comb(test2))
print(comb(test3))



