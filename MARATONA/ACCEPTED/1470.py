def fold(input_tape, pos):
    size = len(input_tape)
    i = pos
    j = pos - 1
    new_tape = []
    while True:
        if i < size and j >= 0:
            new_tape.append(input_tape[i] + input_tape[j])
        elif j >= 0:
            new_tape.append(input_tape[j])
        elif i < size:
            new_tape.append(input_tape[i])
        else:
            break
        i += 1
        j -= 1
    return new_tape

def walk(input_tape, output_tape):
    size = len(input_tape)
    #print input_tape, output_tape, size
    result = False
    if input_tape == output_tape or list(reversed(input_tape)) == output_tape:
        result = True
    else:
        for k in range(1, size):
            result = result or walk(fold(input_tape, k), output_tape)
    return result

while True:
    try:
        N = int(raw_input())
        input_tape = map(int, raw_input().split())
        M = int(raw_input())
        output_tape = map(int, raw_input().split())
        if sum(input_tape) != sum(output_tape):
            print "N"
        elif walk(input_tape, output_tape):
            print "S"
        else:
            print "N"
    except EOFError:
        break