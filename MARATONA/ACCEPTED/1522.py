def attempt(one, two, three, visited):
    #print one, two, three
    if one:
        a = one[0]
    if two:
        b = two[0]
    if three:
        c = three[0]
    if (not one and not two and not three):
        return True
    
    if one and two and three:
        t1 = a + b + c
    else:
        t1 = -1
    if one and two:
        t2 = a + b
    else:
        t2 = -1
    if one and three:
        t3 = a + c
    else:
        t3 = -1
    if two and three:
        t4 = b + c
    else:
        t4 = -1

    result = False

    if t1 % 3 == 0 and not t1 == -1:
        if not visited[len(one)][len(two)][len(three)]:
            visited[len(one)][len(two)][len(three)] = True
            if attempt(one[1:], two[1:], three[1:], visited):
                return True

    if t2 % 3 == 0 and not t2 == -1:
        if not visited[len(one)][len(two)][len(three)+1]:
            visited[len(one)][len(two)][len(three)+1] = True
            if attempt(one[1:], two[1:], three, visited):
                return True
    if t3 % 3 == 0 and not t3 == -1:
        if not visited[len(one)][len(two)+1][len(three)]:
            visited[len(one)][len(two)+1][len(three)] = True
            if attempt(one[1:], two, three[1:], visited):
                return True
    if t4 % 3 == 0 and not t4 == -1:
        if not visited[len(one)+1][len(two)][len(three)]:
            visited[len(one)+1][len(two)][len(three)] = True
            if attempt(one, two[1:], three[1:], visited):
                return True
    return False
    

while True:
    N = int(raw_input())
    if N == 0:
        break
    one, two, three = [], [], []
    visited = [[[False for k in xrange(N+2)] for j in xrange(N+2)] for i in xrange(N+2)]
    for i in xrange(N):
        a, b, c = map(int, raw_input().split())
        if a % 3 != 0:
            one.append(a % 3)
        if b % 3 != 0:
            two.append(b % 3)
        if c % 3 != 0:
            three.append(c % 3)

    total = sum(one+two+three)

    if attempt(one, two, three, visited) and total % 3 == 0: 
        print "1"
    else:
        print "0"