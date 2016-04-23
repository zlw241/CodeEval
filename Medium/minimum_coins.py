

def minimum_coins(amount, denominations):
    solutions = [None for i in range(amount+1)]
    coin_dict = {}
    solutions[0] = 0
    for i in range(1,amount+1):
        available_coins = [c for c in denominations if c <= i]
        coin_dict[i] = min([solutions[i-c]+1 for c in available_coins])
        solutions[i] = min([solutions[i-c]+1 for c in available_coins])
    num_coins = solutions[-1]
    return num_coins


print(minimum_coins(11,[1,3,5]))
# >>> 3
