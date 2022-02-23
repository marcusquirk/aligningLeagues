from findLines import findLines
from getSides import getSides
from subdivideDivs import subdivideDivs
from subsetDistance import subsetDistance
import math
from visualiseSets import visualiseSets


def findBestDiv(num, set, size):
    if size == len(set):
        return [[set]]
    else:
        arrangements = []
        arrangementDistances = []
        minimum = math.inf

        x = [team[1] for team in set]
        y = [team[0] for team in set]
        divLines = findLines(x, y, size=size)

        for divLine in divLines:
            sides = getSides(divLine, x, y)
            arrangements += [subdivideDivs(sides, size)]
            for arrangement in arrangements:
                distance = subsetDistance(arrangement)
                arrangementDistances += [(arrangement, distance)]

        arrangements = sorted(arrangementDistances, key=lambda elem: elem[-1])
        i = 0
        while i < len(arrangements) - 1:
            if math.isclose(arrangements[i][-1], arrangements[i + 1][-1], rel_tol=0.000001):
                arrangements.remove(arrangements[i])
            else:
                i += 1
        arrangements = [arrangement[0] for arrangement in arrangements]
        return arrangements
