import math


def findAngles(x_points, y_points, angle_point_x, angle_point_y):
    listOfAngles = []
    for i in range(len(x_points)):
        delta_x = x_points[i] - angle_point_x
        delta_y = y_points[i] - angle_point_y
        listOfAngles.append([math.atan(delta_x/delta_y), x_points[i], y_points[i]])
    #listOfAngles.sort(reverse=True)
    return listOfAngles