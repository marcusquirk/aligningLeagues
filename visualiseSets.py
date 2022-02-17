from findConvexHull import findConvexHull
import matplotlib.pyplot as plt
from getSides import getSides
from estimateTravel import estimateTravel
import math


def visualiseSets(sets, limits, loaded=False, extent=None, backgroundMap=None, colour=u'#1f77b4'):
    fig, ax = plt.subplots()
    #plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], linewidth=0.5)

    for points in sets:
        x = []
        y = []
        for i in points:
            # Reverse the points back to x-y from lat/long
            x.append(i[0][1])
            y.append(i[0][0])
        plt.scatter(x, y, color=colour)
        edges = findConvexHull(x, y)
        plt.plot(edges[0], edges[1], color=colour)

    if loaded:
        ax.imshow(backgroundMap, extent=extent)

    ax.set_xlim(limits[0], limits[1])
    ax.set_ylim(limits[2], limits[3])
    plt.show()



