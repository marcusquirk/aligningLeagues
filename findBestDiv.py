from findLines import findLines
from getSides import getSides
from subdivideDivs import subdivideDivs
from subsetDistance import subsetDistance


def findBestDiv(num, set, size):
    if size == len(set):
        return [[set]]
    else:
        arrangements = []
        arrangementDistances = []

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
            if arrangements[i][-1] == arrangements[i + 1][-1]:
                arrangements.remove(arrangements[i])
            else:
                i += 1
        arrangements = [arrangement[0] for arrangement in arrangements][:num]
        return arrangements
