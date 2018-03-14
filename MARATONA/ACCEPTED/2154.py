def derive(equation):
    first, second = map(int, equation.split("x"))
    first *= second
    second -= 1
    if second == 0:
        return "%d" % (first)
    elif second == 1:
        return "%dx" % (first)
    else:
        return "%dx%d" % (first, second)

while True:
    try:
        terms = int(raw_input())
        equation = raw_input()
        new_equation = []
        for part in equation.split(" + "):
            new_equation.append(derive(part))
        print " + ".join(new_equation)
    except EOFError:
        break