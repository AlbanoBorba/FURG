import math
 
# A function to print all prime factors of 
# a given number n
def primeFactors(n):
     
    # Print the number of two's that divide n
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i ad divide n
        while n % i== 0:
            primes.append(i)
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        primes.append(n)
    
    return primes

T = int(raw_input())


for i in xrange(T):
    N = int(raw_input())
    factors = primeFactors(N)
    extra = []
    result = 1
    for elem in factors:
        result *= elem
        if factors.count(elem) % 2 == 1 and elem not in extra:
            extra.append(elem)
    for elem in extra:
        result *= elem
    print "Caso #%d: %d" % (i+1, result)
        