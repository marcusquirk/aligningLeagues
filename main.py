import numpy as np
import matplotlib.pyplot as plt
from findConvexHull import findConvexHull
from divideLines import divideLines
from tupleSubtract import tupleSubtract
import math
from csv import reader
from visualiseLines import visualiseLines
from geopy import distance

LEFT = 0
RIGHT = 1
BOTTOM = 0
TOP = 1
NUM_POINTS = 30
ANGLE = math.inf

loaded = False
fileName = input("Choose set of points file: ")
try:
    with open('./csv/' + fileName, 'r') as read_obj:
        csvFile = list(reader(read_obj))
        backgroundMap = plt.imread(csvFile[0][0])
        x, y = [float(num) for num in csvFile[2]], [float(num) for num in csvFile[3]]
        NUM_POINTS =  len(x)
        LEFT, RIGHT, BOTTOM, TOP = float(csvFile[1][0]), float(csvFile[1][1]), float(csvFile[1][2]), float(csvFile[1][3])
        limits = [float(num) for num in csvFile[4]]
        loaded = True
except:
    print("No such file; using random points")
    x, y = np.random.rand(NUM_POINTS)**2.1 * (RIGHT - LEFT) + LEFT, np.random.rand(NUM_POINTS)**1.3 * (TOP - BOTTOM) + BOTTOM
    limits = [LEFT, RIGHT, BOTTOM, TOP]


edges = findConvexHull(x, y)
##plt.plot(edges[0], edges[1])

def drawLines(x, y):
    dividingLines = divideLines(x, y)
    for line in dividingLines:
        plt.plot([line[0][0], line[1][0]], [line[0][1],line[1][1]], linewidth=0.5)

#drawLines(x,y)

dividingLines = divideLines(x, y, ANGLE)

dividingLines = sorted(dividingLines, key = lambda elem: elem[2])

print(distance.distance((y[0],x[0]),(y[1],x[1])))

print("The number of points is", NUM_POINTS)
print("The number of dividing lines is", int(NUM_POINTS * (NUM_POINTS - 1) / 2))
print("The number of equal dividing lines with angle less than", ANGLE, "is", len(dividingLines))

fig, ax = plt.subplots()
plt.scatter(x, y)
if loaded:
    ax.imshow(backgroundMap, extent=[LEFT, RIGHT, BOTTOM, TOP])
ax.set_xlim(limits[0], limits[1])
ax.set_ylim(limits[2], limits[3])
plt.show()

if loaded:
    visualiseLines(dividingLines, plt, x, y, limits, loaded, LEFT, RIGHT, BOTTOM, TOP, backgroundMap)
else:
    visualiseLines(dividingLines, plt, x, y, limits, loaded, LEFT, RIGHT, BOTTOM, TOP)
