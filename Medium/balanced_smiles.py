import re


def balanced_parentheses(string):
    smiley_match = re.compile(r'^([a-z: ]+|:\)|:\()+')
    if string == "":
        return True
    elif string == ":)":
        return True
    elif string == ":(":
        return True
    elif smiley_match.match(string):
        return True
    elif string[0] == "(" and string[-1] == ")":
        return balanced_parentheses(string[1:-1])
    return False


def balanced_smileys(string):
    parens = []
    for i in range(len(string)):
        if (string[i] == "(" or string[i] == ")") and (string[i-1] != ":"):

            parens.append(string[i])
    return parens


print(balanced_smileys(":(("))
print(balanced_smileys("i am sick today (:()"))
print(balanced_smileys("(:)"))
print(balanced_smileys("hacker cup: started :):)"))
print(balanced_smileys(")("))



