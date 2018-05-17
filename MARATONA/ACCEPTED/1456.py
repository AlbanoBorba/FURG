import sys

N = int(raw_input())

for i in range(N):
    tape = [0]
    tape_size = 1
    skip = 0
    pointer = 0
    j = 0
    to_print = ""
    _ = sys.stdin.readline()
    word = sys.stdin.readline()
    commands = sys.stdin.readline()
    loop_begins = []
    c = 0
    while j < len(commands):
        c += 1
        #if c > 800:
            #print list(enumerate(tape)), pointer, commands[j], skip
        if commands[j] == "+" and skip == 0:
            if tape[pointer] < 255:
                tape[pointer] += 1
            else:
                tape[pointer] = 0
        elif commands[j] == "-" and skip == 0:
            if tape[pointer] > 0:
                tape[pointer] -= 1
            else:
                tape[pointer] = 255
        elif commands[j] == ">" and skip == 0:
            if pointer < 29999:
                pointer += 1
                if pointer >= tape_size:
                    try:
                        tape[pointer] = 0
                    except Exception:
                        tape.append(0)
                    tape_size += 1
        elif commands[j] == "<" and skip == 0:
            if pointer > 0:
                pointer -= 1
        elif commands[j] == "." and skip == 0:
            to_print += (unichr(tape[pointer]))
        elif commands[j] == "," and skip == 0:
            try:
                l = word[0]
                word = word[1:]
                tape[pointer] = ord(l)
            except Exception as e:
                tape[pointer] = 0
        elif commands[j] == "[":
            if tape[pointer] == 0:
                skip += 1
                #print skip
            if skip == 0:
                loop_begins.append(j)
                #print loop_begins
        elif commands[j] == "]":
            if skip > 0:
                skip -= 1
            elif tape[pointer] != 0:
                j = loop_begins[-1]
            else:
                loop_begins.pop()
        elif commands[j] == "#" and skip == 0:
            if tape_size < 10:
                for i in range(tape_size):
                    to_print += unichr(tape[i])
                for i in range(10-tape_size):
                    to_print += "0"
            else:
                for i in range(10):
                    to_print += unichr(tape[i])      

        j += 1
    try:
        if ord(to_print[0]) == 10:
            flag = True
        else:
            flag = False
        if flag:
            print "Instancia %d%s\n" % (i+1, to_print)
        else:
            print "Instancia %d\n%s\n" % (i+1, to_print)
    except IndexError:
        print "Instancia %d\n\n" % (i+1)