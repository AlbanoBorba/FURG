def knapsack_with_repetitions(W, wt, val, n):
    dp = [0 for i in xrange(W+1)]
    ans = 0
    for i in xrange(W+1):
        for j in xrange(n):
            if wt[j] <= i:
                dp[i] = max(dp[i], dp[i-wt[j]]+val[j])
    
    #print dp
    return dp[W]