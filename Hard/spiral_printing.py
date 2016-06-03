import sys


def make_matrix(string):
    begin_list = string.split(';')
    rows = int(begin_list[0])
    columns = int(begin_list[1])
    items = begin_list[2].split(' ')
    matrix = []
    for i in range(rows):
        start = i*columns
        end = start+columns
        matrix.append(items[start:end])
    return matrix
    
def spiral(matrix):
    try:
        across = matrix[0]
        order.append(across)
        matrix = matrix[1:]

        down = []
        for i in range(len(matrix)):
            down.append(matrix[i][-1])
            matrix[i] = matrix[i][:-1]
        order.append(down)

        matrix[-1] = matrix[-1][::-1]
        order.append(matrix[-1])
        matrix = matrix[:-1]

        first_index_range = list(range(0,len(matrix))[::-1])
        first_indexes = []
        for i in first_index_range:
            first_indexes.append(matrix[i][0])
            matrix[i] = matrix[i][1:]
        order.append(first_indexes)
        if matrix:
            return spiral(matrix)
        else:
            return order
    except IndexError:
        return order

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip('\n')
        test_matrix = make_matrix(test)
        order = []
        rough = spiral(test_matrix)
        smoov = [' '.join(i) for i in rough if i]
        print(' '.join(smoov))
