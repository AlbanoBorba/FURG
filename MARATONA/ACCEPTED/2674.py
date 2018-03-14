def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(n ** 0.5) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

while True:
    try:
        number = raw_input()
        if is_prime(int(number)):
            flag = True
            for digit in number:
                flag = flag and is_prime(int(digit))
            if flag:
                print "Super"
            else:
                print "Primo"
        else:
            print "Nada"
    except EOFError:
        break