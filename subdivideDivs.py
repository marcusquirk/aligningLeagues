import math

from findLines import findLines
from getSides import getSides
from subsetDistance import subsetDistance


def subdivideDivs(sides, size):
    minimum = math.inf
    count = 0
    bestArrangement = []
    divs = []
    for side in sides:
        if len(side) == size:
            divs += [side]
            count += 1
        else:
            x = [team[1] for team in side]
            y = [team[0] for team in side]
            lines = findLines(x, y, size=size)

    if count == len(sides):
        return sides

    for line in lines:
        newSides = getSides(line, x, y)
        arrangement = divs + subdivideDivs(newSides, size)
        distance = subsetDistance((arrangement))
        if distance < minimum:
            minimum = distance
            bestArrangement = arrangement
    return bestArrangement