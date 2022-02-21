from findBestConf import findBestConf
from findLines import findLines
from getSides import getSides
from subsetDistance import subsetDistance
import math


def findBestDiv(num, set, size):
    x = [team[1] for team in set]
    y = [team[0] for team in set]

    bestDivs = []
    divLines1 = findLines(x, y, size=size)
    minimum = math.inf
    for divLine1 in divLines1:
        sides = getSides(divLine1, x, y)
        for side in sides:
            if len(side) == size:
                div1 = [side]
            else:
                divX = [team[1] for team in side]
                divY = [team[0] for team in side]
                divLines2 = findLines(divX, divY, size=size)
        thisMinimum = math.inf
        for divLine2 in divLines2:
            div23 = getSides(divLine2, divX, divY)
            thisArrangement = div1 + div23

            thisDistance = subsetDistance((thisArrangement))
            if thisDistance < thisMinimum:
                thisMinimum = thisDistance
                thisDiv = thisArrangement

        if thisMinimum < minimum:
            minimum = thisMinimum
            bestDivs = thisDiv

    return bestDivs