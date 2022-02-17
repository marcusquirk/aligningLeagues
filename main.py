import numpy as np
import matplotlib.pyplot as plt
from estimateTravel import estimateTravel
from findLines import findLines
import math
from csv import reader
from findBestLines import findBestLines
from showPoints import showPoints
from visualiseSets import visualiseSets
from getSides import getSides

numSolutions = 5
extent = [0,1,0,1]
NUM_POINTS = 41
ANGLE = math.inf
games = [1.85714286, 1.85714286, 1]

loaded = False
fileName = input("Choose set of points file: ")
try:
    with open('./csv/' + fileName, 'r') as read_obj:
        csvFile = list(reader(read_obj))
        backgroundMap = plt.imread(csvFile[0][0])
        x, y = [float(num) for num in csvFile[2]], [float(num) for num in csvFile[3]]
        names = [name for name in csvFile[4]]
        NUM_POINTS =  len(x)
        extent = [float(csvFile[1][0]), float(csvFile[1][1]), float(csvFile[1][2]), float(csvFile[1][3])]
        limits = [float(num) for num in csvFile[5]]
        loaded = True
except:
    print("No such file; using random points")
    x, y = np.random.rand(NUM_POINTS)**2.1 * \
           (extent[1] - extent[0]) + extent[0], np.random.rand(NUM_POINTS)**1.3 * (extent[3] - extent[2]) + extent[2]
    names = [i for i in range(NUM_POINTS)]
    limits = extent

dividingLines = findLines(x, y, ANGLE)

print("The number of points is", NUM_POINTS)
print("The number of dividing lines is", int(NUM_POINTS * (NUM_POINTS - 1) / 2))
print("The number of equal dividing lines with angle less than", ANGLE, "is", len(dividingLines))

if loaded: showPoints(plt, x, y, limits, loaded, extent, backgroundMap)
else: showPoints(plt,x,y,limits,loaded)

lines = findBestLines(numSolutions, dividingLines, x, y, (games[0], games[2]), names)

if loaded:
    for line in lines:
        sets = getSides(line, x, y, names)
        estimateTravel(([sets[0]], [sets[1]]), games)
        visualiseSets(sets, limits, loaded, extent, backgroundMap)
else:
    for line in lines:
        sets = getSides(line, x, y, names)
        estimateTravel(([sets[0]], [sets[1]]), games)
        visualiseSets(sets, limits)

