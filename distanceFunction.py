from geopy import distance

def distanceFunction(left, right):
    totalDistance = distance.distance((0,0),(0,0))
    for side in left, right:
        for i in range(len(side)):
            for j in range(i+1, len(side)):
                my_distance = distance.distance(side[i], side[j])
                print("Points",side[i],side[j])
                print("Distance",my_distance)
                totalDistance += my_distance
    return(totalDistance)