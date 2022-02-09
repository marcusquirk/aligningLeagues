from operator import itemgetter
import numpy as np
from findAngles import findAngles
from tupleSubtract import tupleSubtract

def findConvexHull(points_x, points_y):
    NUM_POINTS = len(points_x)
    lowest_point_y = min(points_y)
    lowest_point_x = min(points_x)
    for i in range(len(points_y)):
        if points_y[i] == lowest_point_y:
            if points_x[i] >= lowest_point_x:
                lowest_point_x = points_x[i]
                lr_point = i

    starting_point = (points_x[lr_point], points_y[lr_point])
    points_x, points_y = np.delete(points_x, lr_point), np.delete(points_y, lr_point)
    listOfAngles = findAngles(points_x, points_y, starting_point[0], starting_point[1])
    sortedPoints = sorted(listOfAngles, key=itemgetter(0), reverse=True)

    stack = [(sortedPoints[NUM_POINTS - 2][1], sortedPoints[NUM_POINTS - 2][2]), starting_point]

    i = 0

    while i < NUM_POINTS - 1:
        line1 = tupleSubtract(stack[-1], stack[-2])
        line2 = tupleSubtract((sortedPoints[i][1], sortedPoints[i][2]), stack[-2])
        crossProduct = np.cross(line1, line2)
        if crossProduct > 0:
            stack.append((sortedPoints[i][1], sortedPoints[i][2]))
            i += 1
        else:
            stack.pop()

    x_edges = []
    y_edges = []
    for edge in stack:
        x_edges.append(edge[0])
        y_edges.append(edge[1])

    return(x_edges, y_edges)