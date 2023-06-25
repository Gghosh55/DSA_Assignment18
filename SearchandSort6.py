def findMinArrowShots(points):
    if len(points) == 0:
        return 0

    points.sort(key=lambda x: x[1])

    arrows = 1
    end = points[0][1]

    for i in range(1, len(points)):
        if points[i][0] > end:

            arrows += 1
            end = points[i][1]
        else:

            end = min(end, points[i][1])

    return arrows
points = [[10,16],[2,8],[1,6],[7,12]]
print(findMinArrowShots(points))
