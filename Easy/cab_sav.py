import re


def wine_match(wines,letters):
    matched = []
    for w in wines:
        for l in letters:
            if w.count(l) < letters.count(l):
                break
        else:
            matched.append(w)
    if matched:
        return ' '.join(matched)
    return False

                

test1 = 'Cabernet Merlot Noir | ot'
test2 = 'Chardonnay Sauvignon | ann'
test3 = 'Shiraz Grenache | o'
tests = [test1,test2,test3]
for test in tests:
    test = test.split(' | ')
    wines = test[0].split(' ')
    letters = test[1]
    print(wine_match(wines,letters))