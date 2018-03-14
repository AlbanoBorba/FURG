instance = 0
while True:
    instance += 1
    N = int(raw_input())
    if N == 0:
        break
    par = raw_input()
    impar = raw_input()
    print "Teste %d" % instance
    for i in range(N):
        a, b = map(int, raw_input().split())
        if (a + b) % 2 == 0:
            print par
        else:
            print impar
    print