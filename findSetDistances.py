import math

def findSetDistances(left, right):
    totalDistance = 0
    for side in left, right:
        for i in range(len(side)):
            for j in range(i+1, len(side)):
                my_distance = math.sqrt(((side[i][0]-side[j][0])**2)+((side[i][1]-side[j][1])**2))
                totalDistance += my_distance
    return(totalDistance)