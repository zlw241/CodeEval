import itertools


def all_permutations(string):
    sorted_permutations = sorted(list(itertools.permutations(string)))
    sorted_strings = [''.join(i) for i in sorted_permutations]
    return ','.join(sorted_strings)


print(all_permutations('Zu6'))
