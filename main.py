import numpy as np
import matplotlib.pyplot as plt
from estimateTravel import estimateTravel
from findBestDiv import findBestDiv
from findLines import findLines
import math
from csv import reader
from findBestConf import findBestConf
from showPoints import showPoints
from visualiseSets import visualiseSets
from getSides import getSides

numSolutions = 5
extent = [0,1,0,1]
NUM_POINTS = 29
ANGLE = math.inf
struct = [2,1]
games = [2, 1.8, 1]

loaded = False
fileName = input("Choose set of points file: ")
try:
    with open('./csv/' + fileName, 'r') as read_obj:
        csvFile = list(reader(read_obj))
        backgroundMap = plt.imread(csvFile[0][0])
        x, y = [float(num) for num in csvFile[2]], [float(num) for num in csvFile[3]]
        names = [name for name in csvFile[4]]
        NUM_POINTS = len(x)
        extent = [float(csvFile[1][0]), float(csvFile[1][1]), float(csvFile[1][2]), float(csvFile[1][3])]
        limits = [float(num) for num in csvFile[5]]
        loaded = True
except:
    print("No such file; using random points")
    x, y = np.random.rand(NUM_POINTS)**2.1 * \
           (extent[1] - extent[0]) + extent[0], np.random.rand(NUM_POINTS)**1.3 * (extent[3] - extent[2]) + extent[2]
    names = [i for i in range(NUM_POINTS)]
    limits = extent

sizes = [NUM_POINTS//struct[0], NUM_POINTS//struct[0]//struct[1]]
print(sizes)

if loaded:
    showPoints(plt, x, y, limits, loaded, extent, backgroundMap)
else:
    showPoints(plt, x, y, limits)

confLines = findLines(x, y, ANGLE, NUM_POINTS//struct[0])

print("The number of points is", NUM_POINTS)
print("The number of dividing lines is", int(NUM_POINTS * (NUM_POINTS - 1) / 2))
print("The number of equal dividing lines with angle less than", ANGLE, "is", len(confLines))

if struct[0] == 2:
    confLines = findBestConf(numSolutions, confLines, x, y)
    #visualiseSets(getSides(conferences[0],x,y),limits,loaded, extent, backgroundMap)

    bestArrangements = []

    if struct[1] > 0:
        for conferences in confLines:
            thisArrangement = []
            for side in getSides(conferences, x, y):
                print(side)
                thisArrangement += [findBestDiv(1, side, sizes[1])]
            bestArrangements += [thisArrangement]

        if loaded:
            for arrangement in bestArrangements:
                print("League Travel:", estimateTravel(arrangement, games))
                # print("Configuration distance:", estimateTravel(arrangement, games))
                visualiseSets(arrangement, limits, loaded, extent, backgroundMap)

else:
    points = [(y[i], x[i]) for i in range(NUM_POINTS)]
    print(points)
    arrangement = []
    arrangement += [findBestDiv(1, points, sizes[1])]

    if loaded:
        print("League Travel:", estimateTravel(arrangement, games))
        # print("Configuration distance:", estimateTravel(arrangement, games))
        visualiseSets(arrangement, limits, loaded, extent, backgroundMap)