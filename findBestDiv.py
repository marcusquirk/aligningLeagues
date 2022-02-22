from findBestConf import findBestConf
from findLines import findLines
from getSides import getSides
from subdivideDivs import subdivideDivs
from subsetDistance import subsetDistance
import math


def findBestDiv(num, set, size):
    if size == len(set):
        return [set]
    else:
        print(len(set))
        minimum = math.inf

        x = [team[1] for team in set]
        y = [team[0] for team in set]

        divLines = findLines(x, y, size=size)
        for divLine in divLines:
            sides = getSides(divLine, x, y)
            arrangement = subdivideDivs(sides, size)
            distance = subsetDistance((arrangement))
            if distance < minimum:
                minimum = distance
                bestArrangement = arrangement

        return bestArrangement
