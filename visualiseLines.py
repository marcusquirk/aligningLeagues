from findConvexHull import findConvexHull
from tupleSubtract import tupleSubtract
import numpy as np
from findSetDistances import findSetDistances
import math

def visualiseLines(dividingLines, plt, x, y, limits, loaded, LEFT=None, RIGHT=None, BOTTOM=None, TOP=None, backgroundMap=None):

    minimum = math.inf

    for line in dividingLines:

        currentLine = line

        left = []
        right = []
        middle = []

        vector = tupleSubtract(currentLine[1], currentLine[0])
        for i in range(len(x)):
            point = (x[i], y[i])
            vector2 = tupleSubtract(point, currentLine[0])
            crossProduct = np.cross(vector, vector2)
            if crossProduct > 0.0001:
                left.append(point)
            elif crossProduct < -0.0001:
                right.append(point)
            else:
                middle.append(point)

        counter = 0
        while len(right) < len(x) // 2:
            right.append(middle[counter])
            counter += 1
        while len(left) < len(x) // 2:
            left.append(middle[counter])
            counter += 1
        if counter < len(middle):
            left.append(middle[counter])

        thisDistance = findSetDistances(left, right)

        if thisDistance < minimum:
            minimum = thisDistance
            print(minimum)
            bestLine = line

            fig, ax = plt.subplots()
            plt.scatter(x, y)

            plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], linewidth=0.5)

            for side in (left, right):
                sideX = []
                sideY = []
                for i in side:
                    sideX.append(i[0])
                    sideY.append(i[1])
                edges = findConvexHull(sideX, sideY)
                plt.plot(edges[0], edges[1], color=u'#1f77b4')

            if loaded:
                ax.imshow(backgroundMap, extent=[LEFT, RIGHT, BOTTOM, TOP])
            ax.set_xlim(limits[0], limits[1])
            ax.set_ylim(limits[2], limits[3])
            plt.show()


    line = bestLine

    fig, ax = plt.subplots()
    plt.scatter(x, y)

    plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], linewidth=0.5)

    for side in (left, right):
        sideX = []
        sideY = []
        for i in side:
            sideX.append(i[0])
            sideY.append(i[1])
        edges = findConvexHull(sideX, sideY)
        plt.plot(edges[0], edges[1], color=u'#1f77b4')

    if loaded:
        ax.imshow(backgroundMap, extent=[LEFT, RIGHT, BOTTOM, TOP])
    ax.set_xlim(limits[0], limits[1])
    ax.set_ylim(limits[2], limits[3])
    plt.show()


