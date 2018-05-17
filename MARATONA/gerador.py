import random
cases = 10

for i in range(cases):
    N = random.randint(4, 10)
    M = random.randint(3, N*2)
    C = random.randint(2, N-1)
    K = random.randint(C, N-1)
    print (N, M, C, K)
    for j in range(C):
        print (j, j+1, random.randint(1, 250))
    for j in range(M-C):
        ori = random.randint(0, N-1)
        while True:
            dst = random.randint(0, N-1)
            if dst != ori:
                break
        dist = random.randint(1, 250)
        print (ori, dst, dist)

print (0, 0, 0, 0)