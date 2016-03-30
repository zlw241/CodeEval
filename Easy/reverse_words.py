

# reverse the ordering of the words of s, don't reverse
# the letters in any word.
def reverse(s):
    split_s = s.split(' ')
    return ' '.join(split_s[::-1])


