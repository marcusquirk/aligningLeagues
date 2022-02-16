from geopy.distance import distance


def distanceFunction(left, right, games):
    totalDistance = distance(0).miles
    for i in range(len(left)):
        my_distance = distance(0).miles
        for j in range(i+1, len(left)):
            my_distance += distance(left[i][0], left[j][0]).miles*games[0]
        #for j in range(len(right)):
            #my_distance += distance(left[i][0], right[j][0]).miles*games[1]
        #print(left[i], my_distance)
        totalDistance += my_distance
    for i in range(len(right)):
        my_distance = distance((0, 0), (0, 0)).miles
        for j in range(i+1, len(right)):
            my_distance += distance(right[i][0], right[j][0]).miles*games[0]
        #for j in range(len(left)):
            #my_distance += distance(right[i][0], left[j][0]).miles*games[1]
        #print(right[i], my_distance)
        totalDistance += my_distance
    return(totalDistance)