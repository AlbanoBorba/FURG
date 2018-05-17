def count(n):
    digits = 1
    current = 1
    while (current % n != 0):
        current = (current * 10 + 1) % n
        digits += 1 
    return digits

while True:
    try:
        n = int(raw_input())
    except EOFError:
        break
    print count(n)