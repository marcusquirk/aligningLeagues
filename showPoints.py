def showPoints(plt, x, y, limits, extent=None, backgroundMap=None):
    fig, ax = plt.subplots()
    plt.scatter(x, y)
    if backgroundMap.any():
        ax.imshow(backgroundMap, extent=extent)
    ax.set_xlim(limits[0], limits[1])
    ax.set_ylim(limits[2], limits[3])
    plt.show()