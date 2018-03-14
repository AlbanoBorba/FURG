import sys
while True:
    zero = "10-01111"
    one = "10-10111"
    two = "10-11011"
    three = "10-11101"
    four = "10-11110"
    five = "01-01111"
    six = "01-10111"
    seven = "01-11011"
    eight = "01-11101"
    nine = "01-11110"
    final = []
    try:
        num = "%9d" % int(raw_input())
        for digit in num:
            if digit == '0' or digit == ' ':
                final.append([x for x in zero])
            elif digit == '1':
                final.append([x for x in one])
            elif digit == '2':
                final.append([x for x in two])
            elif digit == '3':
                final.append([x for x in three])
            elif digit == '4':
                final.append([x for x in four])
            elif digit == '5':
                final.append([x for x in five])
            elif digit == '6':
                final.append([x for x in six])
            elif digit == '7':
                final.append([x for x in seven])
            elif digit == '8':
                final.append([x for x in eight])
            elif digit == '9':
                final.append([x for x in nine])
        
        for i in xrange(8):
            for j in xrange(9):
                sys.stdout.write(final[j][i])
            print
        print
            
    except EOFError:
        break