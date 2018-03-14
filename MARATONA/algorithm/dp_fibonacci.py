import sys
sys.setrecursionlimit(10000)

fib_array = [0,1]
 
def fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n<=len(fib_array):
        return fib_array[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        fib_array.append(temp_fib)
        return temp_fib
 
# Driver Program
 
print(fibonacci(10**3+3))