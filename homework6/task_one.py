import math


def dist(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


def dists(points):
    return [dist(p1, p2) for p1, p2 in zip(points[:-1], points[1:])]


result = dists([(1, 1), (2, 3), (5, 8)])
s = 0
for i in result:
    result[s] = float('{:.1f}'.format(i))
    s += 1
print(', '.join(map(str, result)))
