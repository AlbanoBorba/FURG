from __future__ import division
import random
import operator
import numpy as np
import matplotlib.pyplot as plt
from math import log, exp, sqrt
from fetcher import getUserInfo


def mean(a):
    return sum(a) / len(a)

def euclideanDistance(point1, point2):
    distance = 0
    for i in range(1, len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return sqrt(distance)

def loadDataset(filename):
    dataset = []
    with open(filename, 'r') as data:
        for line in data:
            content = line.split()

            dataset.append([content[0]] + map(int, content[1:]))
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

def findCloser(user, somap, dims):
    closest_i = 0
    closest_j = 0
    closest = 99496682793
    for i in range(dims):
        for j in range(dims):
            dist = euclideanDistance(user[1:], somap[i][j])
            if dist < closest:
                closest = dist
                closest_i, closest_j = i, j
    return closest_i, closest_j

def randomWeights(mins, maxs, length):
    now = []
    for i in range(length-1):
        now.append(random.uniform(mins[i], maxs[i]))
    return now

def adjust(user, node, learning_rate, influence):
    W = np.asarray(node)
    V = np.asarray(user)
    #print W, V
    Wout = W + (influence*learning_rate*(V-W))
    return Wout.tolist()

def showMatrix(matrix):
    #print np.asarray(matrix)
    nw = []
    for subarray in matrix:
        nw.append(map(np.sum, subarray))
    print np.asarray(nw).shape
    mx = np.max(nw)
    m = np.asarray(nw)
    m_norm = m / mx
    #print m_norm, somap
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.imshow(m_norm)
    plt.show()

def train(iterations=100, dims=10):
    dataset = loadDataset("dataset1")
    mins = getMins(dataset)
    maxs = getMaxs(dataset)
    length = len(dataset[0])
    # initializing weights and constants #
    map_radius = dims/3
    time_constant = iterations/log(map_radius)
    l0 = 0.1
    somap = [[randomWeights(mins,maxs,length) for i in range(dims)] for j in range(dims)]
    history = []
    for i in range(iterations):
        print i
        mtol = -float(i+1/time_constant)
        neighbourhood_radius = map_radius * exp(mtol)
        learning_rate = l0 * exp(mtol)
        for user in dataset:
            closer = list(findCloser(user, somap, dims))
            for i in range(dims):
                for j in range(dims):
                    dist = euclideanDistance(closer, [i, j])
                    radsq = neighbourhood_radius
                    #print closer, i, j
                    #print dist, radsq
                    if dist < dims/3:
                        #print i, j
                        influence = exp(-dist/(2*radsq))
                        somap[i][j] = adjust(user[1:], somap[i][j], learning_rate, influence)

    return somap

somap = train()
showMatrix(somap)
