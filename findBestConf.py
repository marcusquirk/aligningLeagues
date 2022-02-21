import math
from getSides import getSides
from subsetDistance import subsetDistance

def findBestConf(num, dividingLines, x, y):
    lines = []

    for line in dividingLines:
        left, right = getSides(line, x, y)
        thisDistance = subsetDistance((left, right))
        lines.append([line, thisDistance, sorted(left), sorted(right)])

    lines = sorted(lines, key=lambda elem: elem[1])

    i = 0
    while i < len(lines)-1:
        if lines[i][2] == lines[i+1][2] or lines[i][2] == lines[i+1][3]:
            lines.remove(lines[i])
        else:
            i += 1

    lines = [line[0] for line in lines][:num]

    return lines
