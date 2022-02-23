from findLines import findLines
from getSides import getSides


def subdivideDivs(sides, size):
    count = 0
    arrangements = []
    divs = []
    for side in sides:
        if len(side) <= size + 1:
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
        arrangements += divs + subdivideDivs(newSides, size)

    return arrangements