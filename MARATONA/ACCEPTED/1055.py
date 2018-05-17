import operator

cases = int(input())
for c in range(cases):
    elements = list(map(int, input().split()))
    num_elements = elements.pop(0)
    out = []
    elements.sort()
    for i in range(num_elements):
        #print (out)
        if len(out) == 0:
            out.append(elements.pop())
            num_elements -= 1
        else:
            if num_elements > 1:
                cdd = [elements[0], elements[-1]]
                p = []
                p.append(abs(cdd[0] - out[0]))
                p.append(abs(cdd[-1] - out[0]))
                p.append(abs(cdd[0] - out[-1]))
                p.append(abs(cdd[-1] - out[-1]))
                max_index, _ = max(enumerate(p),
                                key=operator.itemgetter(1))
                if max_index == 0:
                    out.insert(0, elements.pop(0))
                elif max_index == 1:
                    out.insert(0, elements.pop())
                elif max_index == 2:
                    out.append(elements.pop(0))
                elif max_index == 3:
                    out.append(elements.pop())
            else:
                if abs(elements[0]-out[0]) > abs(elements[0]-out[-1]):
                    out.insert(0, elements.pop(0))
                else:
                    out.append(elements.pop(0))
    total = 0
    #print (out)
    for i in range(num_elements):
        #print (out[i], out[i+1])
        total += abs(out[i] - out[i+1])
    print ("Case %d: %d" % (c+1, total))
