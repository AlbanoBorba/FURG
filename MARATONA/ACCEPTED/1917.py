def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b
 
while True:
    a, b = map(int, raw_input().split())
    if a==0 and b == 0:
         break
    print a*fibonacci(b+3)