from findConvexHull import findConvexHull
import matplotlib.pyplot as plt


def visualiseSets(sets, limits, loaded=False, extent=None, backgroundMap=None, colour=u'#1f77b4'):
    fig, ax = plt.subplots()
    #plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], linewidth=0.5)
    for conf in sets:
        for divs in conf:
            # Reverse the points back to x-y from lat/long
            x = [team[1] for team in divs]
            y = [team[0] for team in divs]

            plt.scatter(x, y, color=colour)
            edges = findConvexHull(x, y)
            plt.plot(edges[0], edges[1], color=colour)

    if loaded:
        ax.imshow(backgroundMap, extent=extent)

    ax.set_xlim(limits[0], limits[1])
    ax.set_ylim(limits[2], limits[3])
    plt.show()



