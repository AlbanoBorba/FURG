fib = list(reversed([1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]))
l = len(fib)
cases = int(raw_input())
for c in xrange(cases):
    bits = [0 for i in xrange(l)]
    value = int(raw_input())
    for i, f in enumerate(fib):
        if value >= f:
            bits[i] = 1
            value -= f
        if value == 0:
            break
    final = 0
    #print bits, fib
    for i in xrange(len(bits)-1):
        if bits[i] == 1:
            #print fib[i],
            final += fib[i+1]
    print final