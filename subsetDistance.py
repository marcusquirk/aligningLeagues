from geopy.distance import distance


def subsetDistance(sets, games):
    totalDistance = distance(0).miles
    for set in sets:
        for i in range(len(set)):
            my_distance = distance(0).miles
            for j in range(len(set)):
                my_distance += distance(set[i][0], set[j][0]).miles*games[0]
            for otherSet in sets:
                if otherSet != set:
                    for j in range(len(otherSet)):
                        my_distance += distance(set[i][0], otherSet[j][0]).miles*games[1]
            totalDistance += my_distance
    return(totalDistance)