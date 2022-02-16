import math
from getSides import getSides
from distanceFunction import distanceFunction
from visualiseLines import visualiseLines

def findBestLine(dividingLines, plt, x, y, limits, loaded, gamesStructure, names, extent=None, backgroundMap=None):
    minimum = math.inf

    for line in dividingLines:

        left, right = getSides(line, x, y, names)
        thisDistance = distanceFunction(left, right, gamesStructure)

        if thisDistance < minimum:
            print(thisDistance)
            minimum = thisDistance
            bestLine = line


            fig, ax = plt.subplots()
            plt = visualiseLines(line, left, plt, limits, loaded, extent, backgroundMap)
            plt = visualiseLines(line, right, plt, limits, loaded, extent, backgroundMap)
            if loaded:
                ax.imshow(backgroundMap, extent=extent)
            ax.set_xlim(limits[0], limits[1])
            ax.set_ylim(limits[2], limits[3])
            plt.show()



    line = bestLine
    left, right = getSides(line, x, y, names)

    fig, ax = plt.subplots()
    plt = visualiseLines(line, left, plt, limits, loaded, extent, backgroundMap, 'red')
    plt = visualiseLines(line, right, plt, limits, loaded, extent, backgroundMap, 'red')
    if loaded:
        ax.imshow(backgroundMap, extent=extent)
    ax.set_xlim(limits[0], limits[1])
    ax.set_ylim(limits[2], limits[3])
    plt.show()

    return bestLine