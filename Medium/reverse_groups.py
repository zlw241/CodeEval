



def reverse_intervals(string):
    rm_semicolon = string.split(";")
    num_list = [int(i) for i in rm_semicolon[0].split(',')]
    interval = int(rm_semicolon[1])
    remainder = len(num_list)%interval
    separated = [list(reversed(num_list[i:i+interval])) for i in range(0,len(num_list), interval)]
    if remainder > 0:
        separated[-1] = list(reversed(separated[-1]))

    flattened = [str(i) for arr in separated for i in arr]
    return ','.join(flattened)




test_case1 = "1,2,3,4,5;2"
test_case2 = "1,2,3,4,5;3"
test_case3 = "1,2,3,4,5,6,7,8,9;3"

print(reverse_intervals(test_case2))
print(reverse_intervals(test_case1))
print(reverse_intervals(test_case3))