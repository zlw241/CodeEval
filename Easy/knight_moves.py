

def valid_move(position):
    if 1 <= position[0] < 9:
        if 1 <= position[1] < 9:
            return True
    return False

def convert_to_value(string):
    letters = "abcdefgh"
    col = int(string[1])
    row = letters.index(string[0])+1
    return row,col

def convert_to_string(moves):
    letters = "abcdefgh"
    results = []
    for i in moves:
        row,col = i
        str_row = letters[row-1]
        str_col = str(col)
        final = ''.join([str_row,str_col])
        results.append(final)
    return ' '.join(sorted(results))

def get_moves(string):
    moves = []
    pos = convert_to_value(string)
    possible_moves = [(1,2),(1,-2),(-1,2),(-1,-2),
                        (2,1),(2,-1),(-2,1),(-2,-1)]
    for i in possible_moves:
        new_pos = (pos[0]+i[0], pos[1]+i[1])
        if valid_move(new_pos):
            moves.append(new_pos)

    return convert_to_string(moves)


test_cases = ['g2','a1','d6','e5','b1']
for test in test_cases:
    print(get_moves(test))

