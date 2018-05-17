def chinese_remainder(n, a, flag):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        if flag:
            a_i = 1
        sum += a_i * mul_inv(p, n_i) * p
    if flag:
        return sum - 1
    else:
        return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

case = 0
while True:
    case += 1
    try:
        n, a = [], []
        for i in xrange(3):
            x, y = map(int, raw_input().split())
            a.append(x) 
            n.append(y)
        print "Caso %d: %d laranja(s)" % (case, chinese_remainder(n, a, a == [0, 0, 0]))
    except EOFError:
        break