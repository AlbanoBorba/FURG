while True:
    try:
        num = raw_input()
        counters = [0 for i in xrange(10)]
        for digit in num:
            #print digit
            counters[int(digit)] += 1
        most = 0
        mostnum = 0
        for i in xrange(10):
            #print counters, i, counters[i], most
            if counters[i] >= most:
                most = counters[i]
                mostnum = i
        print mostnum
    except EOFError:
        break
    
