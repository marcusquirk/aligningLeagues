from tupleSubtract import tupleSubtract
import numpy as np


def getSides(line, x, y, names):
    """returns the subsets of points from a dividing line
    Parameters:
        line - the dividing line
        x - the x-values of the points
        y - the y-values of the points
        names - the associated names of each point"""

    i_line = line[0][0]
    j_line = line[0][1]

    linePoints = [(x[i_line],y[i_line]),(x[j_line],y[j_line])]

    left = []
    right = [[linePoints[0][::-1], names[i_line]], [linePoints[1][::-1], names[j_line]]]

    vector = tupleSubtract(linePoints[1],linePoints[0])

    for i in range(len(x)):

        if i != i_line and i != j_line:
            point = (x[i], y[i])
            vector2 = tupleSubtract(point, linePoints[0])
            crossProduct = np.cross(vector, vector2)
            if crossProduct > 0:
                # Points are reversed so they can be passed as lat/long to the distance function
                left.append([point[::-1], names[i]])
            else:
                right.append([point[::-1], names[i]])


    return left, right
