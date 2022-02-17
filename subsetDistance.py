from geopy.distance import distance


def subsetDistance(sets):
    totalDistance = distance(0).miles
    for set in sets:
        for i in range(len(set)):
            my_distance = distance(0).miles
            for j in range(len(set)):
                my_distance += distance(set[i], set[j]).miles*2
            for otherSet in sets:
                if otherSet != set:
                    for j in range(len(otherSet)):
                        my_distance += distance(set[i], otherSet[j]).miles
            totalDistance += my_distance
    return(totalDistance)