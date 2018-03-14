factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def last_non_zero_fat(n):

    if n < 5:
        return factorial[n] % 10
    elif n < 10:
        return (factorial[n] % 100) / 10
    elif int(str(n)[-2]) % 2 == 0:
        return (6*last_non_zero_fat(n/5)*last_non_zero_fat(n%10)) % 10
    else:
        return (4*last_non_zero_fat(n/5)*last_non_zero_fat(n%10)) % 10

instance = 0
while True:
    instance += 1
    try:
        n = int(raw_input())
    except EOFError:
        break
    print "Instancia %d" % instance
    print last_non_zero_fat(n)
    print