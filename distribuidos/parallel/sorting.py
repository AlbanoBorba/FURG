import time
import numpy as np
import threading
from threading import Thread
import matplotlib.pyplot as plt


def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low , high):
 
        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

def quickSort(arr,low,high):
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def randomArr(low, high, elements):
    arr = np.random.randint(low, high, elements)
    return arr.tolist()

def sequentialQuick(group):
    begin = time.time()
    for arr in group:
        n = len(arr)
        quickSort(arr, 0, n-1)
    return time.time() - begin

def sequentialBubble(group):
    begin = time.time()
    for arr in group:
        n = len(arr)
        bubbleSort(arr)
    return time.time() - begin

def oneQuick(group, start, num_threads):
    size = len(group)
    for i in range(start, size, num_threads):
        n = len(group[i])
        quickSort(group[i], 0, n-1)

def oneBubble(group, start, num_threads):
    size = len(group)
    for i in range(start, size, num_threads):
        bubbleSort(group[i])

def parallelQuick(group, num_threads):
    threads = []
    flag = False
    begin = time.time()
    for i in xrange(num_threads):
        threads.append(Thread(target=oneQuick, args=(group, i, num_threads)))
    for thread in threads:
        thread.start()
    while True:
        for thread in threads:
            if not thread.isAlive():
                flag = False
            else:
                flag = True
        if not flag:
            return time.time() - begin

def parallelBubble(group, num_threads):
    threads = []
    begin = time.time()
    for i in xrange(num_threads):
        threads.append(Thread(target=oneBubble, args=(group, i, num_threads)))
    for thread in threads:
        thread.start()
    while True:
        for thread in threads:
            if not thread.isAlive():
                flag = False
            else:
                flag = True
        if not flag:
            return time.time() - begin


def main():
    M = 1000
    N = 2
    num_threads = 16

    group = []
    timeSeqQuick = []
    timeSeqBubble = []
    timeParQuick = []
    timeParBubble = []
    ns = []

    for i in xrange(10):
        ns.append(N)
        for i in xrange(M):
            group.append(randomArr(0, 10000, N))
        group2 = group
        group3 = group
        group4 = group
        timeSeqQuick.append(sequentialQuick(group))
        print "foi quickseq"
        timeSeqBubble.append(sequentialBubble(group))
        print "foi bubbleseq"
        timeParQuick.append(parallelQuick(group, num_threads))
        print "foi quickpar"
        timeParBubble.append(parallelBubble(group, num_threads))
        print "foi bubblepar"
        
        N *= 2


    print ns
    print timeSeqQuick
    print timeSeqBubble
    print timeParQuick
    print timeParBubble
    plt.plot(ns, timeSeqBubble, 'r', ns, timeSeqQuick, 'b', ns, timeParBubble, 'g', ns, timeParQuick, 'm')
    plt.show()

main()