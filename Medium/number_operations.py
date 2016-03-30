import sys
from itertools import permutations

def op_helper(numlist):
    results_cache = []
    results_cache.append(numlist[0]*numlist[1])
    results_cache.append(numlist[0]+numlist[1])
    results_cache.append(numlist[0]-numlist[1])
    for i in range(2,5):
        new_cache = []
        for c in results_cache:
            new_cache.append(c*numlist[i])
            new_cache.append(c-numlist[i])
            new_cache.append(c+numlist[i])
        results_cache = new_cache
    return results_cache


def operations(numberstring):
    numbers = numberstring.split(' ')
    numbers = [int(i) for i in numbers]
    all_results = []
    possible_orderings = [list(i) for i in list(permutations(numbers))]
    for nums in possible_orderings:
        all_results += op_helper(nums)
        if 42 in all_results:
            return "YES"
    return "NO"


# for test in test_cases:
#     test = test.rstrip('\n')
#     print(operations(test))


