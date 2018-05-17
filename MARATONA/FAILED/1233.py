import math
 
# A function to print all prime factors of 
# a given number n
def primeFactors(n):
    factors = {}
    # Print the number of two's that divide n
    while n % 2 == 0:
        factors[2] = 1
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i ad divide n
        while n % i== 0:
            factors[i] = 1
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        factors[n] = 1
    return factors

while True:
    try:
        N = int(raw_input())
        factors = primeFactors(N)
        result = 1
        for key, value in factors.iteritems():
            result *= key
        print result
    except EOFError:
        break