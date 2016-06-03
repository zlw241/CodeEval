from itertools import combinations 
import sys

def range_combos(palindrome_range):
    y = [int(i) for i in palindrome_range.split(' ')]
    x = range(y[0], y[1]+2)
    indexes = list(combinations(x, 2))
    results = []
    for i in indexes:
        results.append(range(i[0],i[1]))
    return results 

def count_palindromes(results):
    count = 0
    for int_range in results:
        palindromes = 0
        for i in int_range:
            i = str(i)
            if i == i[::-1]:
                palindromes += 1
        if palindromes % 2 == 0:
            count += 1
    return count 

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.rstrip('\n')
        ranges = range_combos(test)
        result = count_palindromes(ranges)
        print result 
