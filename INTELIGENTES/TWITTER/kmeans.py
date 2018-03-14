from __future__ import division
import random
import math
import operator
import matplotlib.pyplot as plt
from fetcher import getUserInfo

def mean(a):
    return sum(a) / len(a)

def euclideanDistance(point1, point2):
    distance = 0
    for i in range(1, len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

def loadDataset(filename):
    dataset = []
    with open(filename, 'r') as data:
        for line in data:
            content = line.split()

            dataset.append([content[0]] + map(int, content[1:-1]))
    return dataset

def getMins(dataset):
    mins = []
    for i in range(1, len(dataset[0])):
        now = []
        for user in dataset:
            now.append(user[i])
        mins.append(min(now))
    return mins

def getMaxs(dataset):
    maxs = []
    for i in range(1, len(dataset[0])):
        now = []
        for user in dataset:
            now.append(user[i])
        maxs.append(max(now))
    return maxs

def findCloser(user, avgs):
    closest_i = 0
    closest = 99496682793
    for i in range(len(avgs)):
        dist = euclideanDistance(user[1:], avgs[i])
        if dist < closest:
            closest = dist
            closest_i = i
    return closest_i

def newAverages(groups):
    avgs = []
    k = len(groups[0])
    for i in range(len(groups)):
        z = map(list, zip(*groups[i]))
        avgs.append(map(mean, z[1:]))
    return avgs

def train(num_epochs=100, k=3):
    dataset = loadDataset("dataset1")
    mins = getMins(dataset)
    maxs = getMaxs(dataset)
    groups = [[] for x in range(k)]
    old = []
    avgs = []
    history = []
    print "alow"
    ## initialize averages ##
    for i in range(k):
        now = []
        for i in range(len(dataset[0])-1):
            now.append(random.uniform(mins[i], maxs[i]))
        avgs.append(now)
        old.append([0]*(len(dataset[0])-1))
    for i in range(num_epochs):
        print "epoch %d" % i
        for user in dataset:
            group = findCloser(user, avgs)
            groups[group].append(user)
        old = avgs
        avgs = newAverages(groups)
        o = sum(map(sum, old))
        n = sum(map(sum, avgs))
        history.append(abs(o - n))
    return avgs, history, groups

plt.figure(1)
averages, history, groups = train(k=3)
test_username = raw_input("Digite o nome do usuario a ser testado: ")
test_user = getUserInfo(test_username)[:-1]
group = findCloser(test_user, averages)

## plotting groups ##
group0 = map(list, (zip(*groups[0])))
plt.scatter(group0[1], group0[2], color='red')
group1 = map(list, (zip(*groups[1])))
plt.scatter(group1[1], group1[2], color='blue')
group2 = map(list, (zip(*groups[2])))
plt.scatter(group2[1], group2[2], color='green')
colors = ["r", "b", "g"]
## plotting averages ##
plt.plot(averages[0][0], averages[0][1], "*r")
plt.plot(averages[1][0], averages[1][1], "*b")
plt.plot(averages[2][0], averages[2][1], "*g")
print colors[group]

## plotting test user ##
plt.plot(test_user[1], test_user[2], "^"+colors[group])
plt.figure(2)
plt.plot(history)
plt.show()
