import math
import sys

sys.setrecursionlimit(10000)

primes = {}
facts = [-1 for x in range(1000)]
facts[0] = 1
facts[1] = 1
"""
def fac(number):
    if number == 1 or number == 0:
        return 1
    else:
        return n*fac(n-1)
"""
def primeFactors(n):
     
    # Print the number of two's that divide n
    while n % 2 == 0:
        primes[2] = 1
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i ad divide n
        while n % i== 0:
            primes[i] = 1
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        primes[n] = 1

despojados = 0
n = int(raw_input())
primeFactors(n)
primos = list(primes.keys())
if len(primos) < 2:
    print 0
else:
    m = len(primos)
    #print facts
    #print m
    for i in range(2, m+1):
        #print m, i, m-i
        despojados += math.factorial(m)/(math.factorial(i)*math.factorial(m-i))
    print despojados