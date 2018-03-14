while True:
    try:
        people = int(raw_input())
        start = map(int, raw_input().split())
        finish = map(int, raw_input().split())
    except EOFError:
        break
    
    count = 0
    i = people-1
    while i >= 0:
        should_be = start.index(finish[i])
        #print finish[i], i, should_be
        #print start, finish
        if should_be > i:
            count += should_be - i
            finish.insert(should_be, finish.pop(i))
            i = should_be - 1
        i -= 1
    print count