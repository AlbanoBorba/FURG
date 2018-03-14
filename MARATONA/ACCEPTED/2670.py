a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

l = []
l.append(b*2 + c*4)
l.append(a*2 + c*2)
l.append(a*4 + b*2)
print min(l)