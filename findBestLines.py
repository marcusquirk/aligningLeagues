import math
from getSides import getSides
from subsetDistance import subsetDistance

def findBestLines(num, dividingLines, x, y, games, names):
    lines = []

    for line in dividingLines:
        left, right = getSides(line, x, y, names)
        thisDistance = subsetDistance((left, right), games)
        lines.append([line, thisDistance])

    lines = sorted(lines, key=lambda elem: elem[1])
    i = 0
    while i < len(lines)-1:
        if math.isclose(lines[i][1], lines[i+1][1], rel_tol=0.00001):
            lines.remove(lines[i])
        else:
            i += 1

    lines = [line[0] for line in lines][:num]

    return lines
