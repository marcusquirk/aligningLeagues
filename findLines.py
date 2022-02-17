from tupleSubtract import tupleSubtract
import numpy as np
import math


def findLines(points_x, points_y, angle, size=None):
    if not size:
        size = len(points_x)//2
    numPoints = len(points_x)
    listOfLines = []
    for i in range(numPoints):
        for j in range(numPoints):
            numLeft = 0
            numRight = 0
            if j != i:
                vector1 = tupleSubtract((points_x[j], points_y[j]), (points_x[i],points_y[i]))
                if abs(math.atan(vector1[1]/vector1[0])) < angle:
                    for k in range(numPoints):
                        vector2 = tupleSubtract((points_x[k], points_y[k]),(points_x[i],points_y[i]))
                        crossProduct = np.cross(vector1, vector2)
                        if crossProduct > 0:
                            numLeft += 1
                        elif crossProduct < 0:
                            numRight += 1
                    if numLeft == size or numRight == size-2:
                        listOfLines.append(((i,j), math.atan(vector1[1]/vector1[0])))
    return listOfLines
