from findConvexHull import findConvexHull
from getSides import getSides
from distanceFunction import distanceFunction
import math


def visualiseLines(line, points, plt, limits, loaded, extent=None, backgroundMap=None, colour=u'#1f77b4'):

    #plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], linewidth=0.5)

    x = []
    y = []
    for i in points:
        # Reverse the points back to x-y from lat/long
        x.append(i[0][1])
        y.append(i[0][0])
    plt.scatter(x, y, color=colour)
    edges = findConvexHull(x, y)
    plt.plot(edges[0], edges[1], color=colour)

    return plt



