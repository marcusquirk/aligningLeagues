import numpy as np
import matplotlib.pyplot as plt
from findConvexHull import findConvexHull
from divideLines import divideLines
from tupleSubtract import tupleSubtract
import math
from csv import reader
from visualiseLines import findBestLines
from showPoints import showPoints
from geopy import distance

extent = [0,1,0,1]
NUM_POINTS = 30
ANGLE = math.inf
gamesStructure = [3.71,2]

backgroundMap = None
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
except:
    print("No such file; using random points")
    x, y = np.random.rand(NUM_POINTS)**2.1 * \
           (extent[1] - extent[0]) + extent[0], np.random.rand(NUM_POINTS)**1.3 * (extent[3] - extent[2]) + extent[2]
    limits = extent

def drawLines(x, y):
    dividingLines = divideLines(x, y,ANGLE)
    for line in dividingLines:
        plt.plot([line[0][0], line[1][0]], [line[0][1],line[1][1]], linewidth=0.5)

#drawLines(x,y)

dividingLines = divideLines(x, y, ANGLE)

#dividingLines = sorted(dividingLines, key = lambda elem: elem[2])

print("The number of points is", NUM_POINTS)
print("The number of dividing lines is", int(NUM_POINTS * (NUM_POINTS - 1) / 2))
print("The number of equal dividing lines with angle less than", ANGLE, "is", len(dividingLines))

showPoints(plt, x, y, limits, extent, backgroundMap)

if backgroundMap.any():
    findBestLines(dividingLines, plt, x, y, limits, gamesStructure, extent, backgroundMap,
                  names)
else:
    findBestLines(dividingLines, plt, x, y, limits, gamesStructure, extent, names)
