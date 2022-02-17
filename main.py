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
struct = [2,3]
games = [2, 1.8, 1]

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

sizes = [NUM_POINTS//struct[0], NUM_POINTS//struct[0]//struct[1]]

if loaded:
    showPoints(plt, x, y, limits, loaded, extent, backgroundMap)
else:
    showPoints(plt, x, y, limits)

confLines = findLines(x, y, ANGLE, NUM_POINTS//struct[0])

print("The number of points is", NUM_POINTS)
print("The number of dividing lines is", int(NUM_POINTS * (NUM_POINTS - 1) / 2))
print("The number of equal dividing lines with angle less than", ANGLE, "is", len(confLines))

conferences = findBestLines(numSolutions, confLines, x, y)
visualiseSets(getSides(conferences[0],x,y),limits,loaded, extent, backgroundMap)

for line in conferences:
    sets = getSides(line,x,y)
    for set in sets:
        confX = []
        confY = []
        for team in set:
            confX.append(team[1])
            confY.append(team[0])
        divLines1 = findLines(confX, confY, size=sizes[1])
        for line in divLines1:
            print(confX)
            divs = getSides(line, confX, confY)
            for div in divs:
                if len(div) == sizes[1]:
                    finalDivs = [div]
                    print(finalDivs)
                else:
                    divX = []
                    divY = []
                    for team in div:
                        divX.append(team[1])
                        divY.append(team[0])
            divLine2 = findBestLines(1,findLines(divX, divY, size=sizes[1]), divX, divY)[0]
            toBeAppended = getSides(divLine2, divX, divY)
            finalDivs.append(toBeAppended[0])
            finalDivs.append(toBeAppended[1])
            visualiseSets(finalDivs, limits, loaded, extent, backgroundMap)
        #divisions = findBestLines(numSolutions, divLines, confX, confY, names)

if loaded:
    for line in conferences:
        sets = getSides(line, x, y)
        print("Configuration distance:", estimateTravel(([sets[0]], [sets[1]]), games))
        print(sets)
        visualiseSets(sets, limits, loaded, extent, backgroundMap)
else:
    for line in conferences:
        sets = getSides(line, x, y)
        estimateTravel(([sets[0]], [sets[1]]), games)
        visualiseSets(sets, limits)

