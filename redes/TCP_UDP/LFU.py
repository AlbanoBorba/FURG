accesses = []*20
actual = [-1, -1, -1]
count = 3

while True:
    new = input()
    if new in actual:
        continue
    elif count < 3:
        actual[count] = new
    else:
        if accesses[actual[0]] < accesses[actual[1]]
            and accesses[actual[0]] < accesses[actual[2]]:
            actual[0] = new
        elif accesses[actual[1]] < accesses[actual[0]]
            and accesses[actual[1]] < accesses[actual[2]]:
            actual[1] = new
        else:
            actual[2] = new
