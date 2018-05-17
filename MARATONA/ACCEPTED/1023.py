import math

city = 1
while True:
    houses = int(raw_input())
    if houses == 0:
        break
    cons = [0] * 210
    tc, tp = 0, 0
    for i in xrange(houses):
        residents, consumption = map(int, raw_input().split())
        cons[consumption/residents] += residents
        tc += consumption
        tp += residents
    if city != 1:
        print
    print "Cidade# %d:" % city
    for i in xrange(201):
        if cons[i] > 0:
            print "%d-%d" % (cons[i], i),
    print
    avg = tc/(tp*1.0)
    #print "%.3f" % avg
    nv = avg * 100
    ni = int(nv)
    result = float(ni)/100.0
    print "Consumo medio: %.2f m3." % result
    city += 1