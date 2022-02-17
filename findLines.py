from tupleSubtract import tupleSubtract
import numpy as np
import math


def findLines(x, y, angle=math.inf, size=None):
    if not size:
        size = len(x) // 2
    numPoints = len(x)
    listOfLines = []
    for i in range(numPoints):
        for j in range(numPoints):
            numLeft = 0
            numRight = 0
            if j != i:
                vector1 = tupleSubtract((x[j], y[j]), (x[i], y[i]))
                if abs(math.atan(vector1[1]/vector1[0])) < angle:
                    for k in range(numPoints):
                        vector2 = tupleSubtract((x[k], y[k]), (x[i], y[i]))
                        crossProduct = np.cross(vector1, vector2)
                        if crossProduct > 0:
                            numLeft += 1
                        elif crossProduct < 0:
                            numRight += 1
                    if numLeft == size or numRight == size-2:
                        listOfLines.append(((i,j), math.atan(vector1[1]/vector1[0])))
    return listOfLines
