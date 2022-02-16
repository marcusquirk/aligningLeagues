from tupleSubtract import tupleSubtract
import numpy as np


def getSides(line, x, y, names):
    """returns the subsets of points from a dividing line
    Parameters:
        line - the dividing line
        x - the x-values of the points
        y - the y-values of the points
        names - the associated names of each point"""


    left = []
    right = []
    middle = []

    vector = tupleSubtract(line[1], line[0])
    for i in range(len(x)):
        point = (x[i], y[i])
        vector2 = tupleSubtract(point, line[0])
        crossProduct = np.cross(vector, vector2)
        if crossProduct > 0.000001:
            # Points are reversed so they can be passed as lat/long to the distance function
            left.append([point[::-1], names[i]])
        elif crossProduct < -0.000001:
            right.append([point[::-1], names[i]])
        else:
            middle.append([point[::-1], names[i]])

    counter = 0
    while len(right) < len(x) // 2:
        right.append(middle[counter])
        counter += 1
    while len(left) < len(x) // 2:
        left.append(middle[counter])
        counter += 1
    if counter < len(middle):
        left.append(middle[counter])

    return left, right