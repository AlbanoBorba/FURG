import math
import sys

sys.setrecursionlimit(100000)

# A function to print all prime factors of 
# a given number n
def primeFactors(n):
    # Print the number of two's that divide n
    primes = []
    last = 2
    tmp = 1
    while n % 2 == 0:
        tmp *= 2
        n = n / 2
    primes.append(tmp)
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i ad divide n
        while n % i == 0:
            if i != last:
                primes.append(i)
            else:
                primes[-1] *= i
            last = i
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        primes.append(n)
    return primes

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

def lcm(a, b):
    return a*b / gcd(a, b)

def array_lcm(arr, L):
    mmc = arr[0]
    for i in range(1, len(arr)):
        if mmc > L:
            break
        if mmc % arr[i] != 0:
            mmc = lcm(mmc, arr[i])
    return mmc

N, L = map(int, raw_input().split())
arr = map(int, raw_input().split())
mmc = array_lcm(arr, L)
#print mmc
if mmc > L:
    print 1
else:
    new_value = mmc*(L / mmc)
    #print new_value
    factors = primeFactors(new_value)
    #print factors
    ans = 1

    for factor in factors:
        flag = True
        for num in arr:
            if num % factor == 0:
                flag = False
                break
        if flag:
            ans *= factor
        
    print ans