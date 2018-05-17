def knapsack_with_repetitions(W, wt, val, n):
    dp = [0 for i in xrange(W+1)]
    ans = 0
    for i in xrange(W+1):
        for j in xrange(n):
            if wt[j] <= i:
                dp[i] = max(dp[i], dp[i-wt[j]]+val[j])
    
    #print dp
    return dp[W]

instance = 0
while True:
    instance += 1
    N, T = map(int, raw_input().split())
    if N == 0 and T == 0:
        break
    times = []
    scores = []
    for i in xrange(N):
        t, s = map(int, raw_input().split())
        times.append(t)
        scores.append(s)
    print "Instancia %d" % instance
    print knapsack_with_repetitions(T, times, scores, len(times))
    print