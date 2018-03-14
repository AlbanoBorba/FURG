def isSubsetSum(arr, n, tot):
    
    # The value of subset[i%2][j] will be true 
    # if there exists a subset of tot j in 
    # arr[0, 1, ...., i-1]
    subset = [ [False for j in range(tot + 1)] for i in range(3) ]
  
    for i in range(n + 1):
        for j in range(tot + 1):
            # A subset with tot 0 is always possible 
            if (j == 0):
                subset[i % 2][j] = True
  
            # If there exists no element no tot 
            # is possible 
            elif (i == 0):
                subset[i % 2][j] = False
            elif (arr[i - 1] <= j):
                subset[i % 2][j] = subset[(i + 1) % 2][j - arr[i - 1]] or subset[(i + 1) 
                                                                               % 2][j]
            else:
                subset[i % 2][j] = subset[(i + 1) % 2][j]
                 
    #print subset
    return subset[n % 2][tot]

instance = 0
while True:
    instance += 1
    X, Y, N = map(int, raw_input().split())
    if X == Y == N == 0:
        break
    nums = []
    print "Teste %d" % instance
    for i in xrange(N):
        nums.append(int(raw_input()))
    total = sum(nums)
    b = (X + total - Y)/2
    a = total - b
    if X + a != Y + b or a < 0 or b < 0 or a > total or b > total:
        print "N"
    else:
        if isSubsetSum(nums, len(nums), a):
            print "S"
        else:
            print "N"
    print