

def distances(houses):
    houses = [int(h) for h in houses.split(' ')][1:]
    minimal_distance = None
    for i in range(min(houses), max(houses)):
        distance_sum = sum([abs(i-h) for h in houses])
        if minimal_distance is None:
            minimal_distance = distance_sum
        else:
            if distance_sum < minimal_distance:
                minimal_distance = distance_sum
    return minimal_distance


print(distances('3 3 5 7'))
print(distances('4 3 3 5 7'))
print(distances('3 20 30 40'))