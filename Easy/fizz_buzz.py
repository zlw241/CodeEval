


def fizzbuzz(f,b,upper_limit):
    result = []
    append = result.append
    for i in range(1,upper_limit+1):
        if i % (f*b) == 0:
            i = "FB"
        elif i % f == 0:
            i = "F"
        elif i % b == 0:
            i = "B"
        append(str(i))
    return ' '.join(result)


print(fizzbuzz(3,5,100))