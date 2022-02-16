from findConvexHull import findConvexHull
from getSides import getSides
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


