doors = [0]*101
def toggle(index):
    if doors[index] == 0:
        doors[index] = 1
    else:
        doors[index] = 0

for stride in xrange(1, 101):
    print doors[1:]
    for i in xrange(0, 101, stride):
        print i,
        toggle(i)
    print

print doors[1:]
