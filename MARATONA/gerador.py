import random
cases = 1000

for i in xrange(cases):
    N = random.randint(1, 15)
    print N
    for j in xrange(N):
        print random.randint(0, 9)
        print random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)
        print random.randint(0, 9)
print 0