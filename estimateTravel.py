from geopy.distance import distance


def estimateTravel(sets, games):
    totalDistance = distance(0).miles
    for thisConf in sets:
        for thisDiv in thisConf:
            for i in range(len(thisDiv)):
                my_distance = distance(0).miles
                for j in range(len(thisDiv)):
                    my_distance += distance(thisDiv[i], thisDiv[j]).miles*games[0]
                for otherDiv in thisConf:
                    if otherDiv != thisDiv:
                        for j in range(len(otherDiv)):
                            my_distance += distance(thisDiv[i], otherDiv[j]).miles*games[1]
                for otherConf in sets:
                    if otherConf != thisConf:
                        for otherDiv in otherConf:
                            for j in range(len(otherDiv)):
                                my_distance += distance(thisDiv[i], otherDiv[j]).miles*games[2]
                #print(thisDiv[i][1], my_distance)
                totalDistance += my_distance
    return(totalDistance)