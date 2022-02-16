from findConvexHull import findConvexHull
from tupleSubtract import tupleSubtract
import numpy as np
from distanceFunction import distanceFunction
import math


def visualiseLines(line, left, right, plt, limits, extent=None, backgroundMap=None, colour=u'#1f77b4'):
    fig, ax = plt.subplots()
    plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], linewidth=0.5)

    for side in (left, right):
        sideX = []
        sideY = []
        for i in side:
            # Reverse the points back to x-y from lat/long
            sideX.append(i[0][1])
            sideY.append(i[0][0])
        plt.scatter(sideX, sideY, color=colour)
        edges = findConvexHull(sideX, sideY)
        plt.plot(edges[0], edges[1], color=colour)

    if backgroundMap.any():
        ax.imshow(backgroundMap, extent=extent)
    ax.set_xlim(limits[0], limits[1])
    ax.set_ylim(limits[2], limits[3])
    plt.show()


def getSides(line, x, y, names):
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


def findBestLines(dividingLines, plt, x, y, limits, gamesStructure, extent=None, backgroundMap=None, names=None):

    minimum = math.inf

    for line in dividingLines:

        left, right = getSides(line,x,y,names)
        thisDistance = distanceFunction(left, right, gamesStructure)

        if thisDistance < minimum:
            print(thisDistance)
            minimum = thisDistance
            bestLine = line
            visualiseLines(line, left, right, plt, limits, extent, backgroundMap)

    line = bestLine
    left,right = getSides(line,x,y,names)

    visualiseLines(line, left, right, plt, limits, extent, backgroundMap, 'red')


