import math

def distance_between(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


instances = int(raw_input())
for instance in xrange(instances):
    masters = int(raw_input())
    homes = []
    for i in xrange(masters):
        x, y = map(int, raw_input().split())
        homes.append((x, y))
    distance_matrix = [[0 for j in xrange(masters)] for i in xrange(masters)]
    for i in xrange(masters):
        for j in xrange(i, masters):
            dist = round(distance_between(homes[i], homes[j]), 2)
            distance_matrix[i][j] = dist
            distance_matrix[j][i] = dist 
    for elem in distance_matrix:
        print elem
    print