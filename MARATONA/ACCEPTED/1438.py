import sys

sys.setrecursionlimit(100000)

def remove_box(stacks, c, h, top, right, came_from):
    l, r = 99999, 99999
    if h+1 > top or stacks[c][h+1] == 0:
        if c+1 > right or stacks[c+1][h] == 0:
            to_remove_this = 0 if stacks[c][h] == 1 else 1
        elif c-1 < 0 or stacks[c-1][h] == 0:
            to_remove_this = 0 if stacks[c][h] == 1 else 1
        else:
            if came_from != "right":
                r = remove_box(stacks, c+1, h, top, right, "left")
            if came_from != "left":
                l = remove_box(stacks, c-1, h, top, right, "right")
            to_remove_this = 1 + min(l, r) if stacks[c][h] != 1 else min(l, r)
    else:
        t = remove_box(stacks, c, h+1, top, right, "bottom")
        to_remove_this = 1 + t if stacks[c][h] != 1 else t
        #print to_remove_this, c, right, h
        if 0 < c < right and stacks[c+1][h] != 0 and stacks[c-1][h] != 0:
            r = remove_box(stacks, c+1, h, top, right, "left")
            l = remove_box(stacks, c-1, h, top, right, "right")
            to_remove_this += 1 + min(l, r) if stacks[c][h] != 1 else min(l, r)
        #print to_remove_this
    #print "to remove %d from position (%d, %d) costs %d" % (stacks[c][h], c, h, to_remove_this)
    stacks[c][h] = 0
    return to_remove_this

while True:
    N, P = map(int, raw_input().split())
    if N == P == 0:
        break
    heights = [0 for x in xrange(P)]
    c = 0
    for i in range(P):
        column = map(int, raw_input().split())
        h = 0
        heights[c] = column[0]
        for box in column[1:]:
            if box == 1:
                col, height = c, h + 1
            h += 1
        c += 1
    
    left, right = 0, 0
    for i in xrange(col-1, -1, -1):
        #print "hehe", heights[i], height
        #print i, 
        if heights[i] < height:
            break
        left += heights[i] - (height - 1)
        #print left
    for i in xrange(col+1, P):
        #print "hehe", heights[i], height
        #print i,
        if heights[i] < height:
            break
        right += heights[i] - (height - 1)
        #print right
    #print left, right
    print heights[col] - (height) + min(left, right)