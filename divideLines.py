from tupleSubtract import tupleSubtract
import numpy as np
import math

BIG = 0

def divideLines(points_x, points_y, angle):
    numPoints = len(points_y)
    listOfLines = []
    for i in range(numPoints):
        for j in range(numPoints):
            numLeft = 0
            numMiddle = 0
            if j != i:
                vector1 = tupleSubtract((points_x[j], points_y[j]), (points_x[i],points_y[i]))
                if abs(math.atan(vector1[1]/vector1[0])) < angle:
                    for k in range(numPoints):
                        vector2 = tupleSubtract((points_x[k], points_y[k]),(points_x[i],points_y[i]))
                        crossProduct = np.cross(vector1, vector2)
                        if crossProduct > 0:
                            numLeft += 1
                        elif crossProduct == 0:
                            numMiddle += 1
                    if numLeft + numMiddle >= numPoints/2 >= numLeft:
                        listOfLines.append(
                            ((points_x[i]+vector1[0]*BIG, points_y[i]+vector1[1]*BIG),
                             (points_x[j]-vector1[0]*BIG, points_y[j]-vector1[1]*BIG),
                             math.atan(vector1[1]/vector1[0])))
    return listOfLines
