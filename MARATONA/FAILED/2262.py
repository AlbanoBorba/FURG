def is_valid(thingy):
    if thingy[0] != 1:
        return False
    for i in range(len(thingy)-1):
        if thingy[i+1] - thingy[i] != 1:
            return False
    return True

def merge(a, b):
    tmp = 0
    final = []
    while True:
        if not a:
            final = b + final
            break
        if not b:
            final = a + final
            break
        if a[-1] > b[-1]:
            final.insert(0, a.pop())
            tmp += 1
        elif b[-1] > a[-1]:
            final.insert(0, b.pop())
            tmp += 1
        else:
            return None, None
    #print final
    return final, tmp

def calculate_difference(a, b):
    count = 0
    a_index = len(a) - 1
    b_index = len(b) - 1
    #print a, b
    if a[a_index] > b[b_index]:
        last_value = a[a_index]
        last = 'a'
        a_index -= 1
    elif a[a_index] < b[b_index]:
        last_value = b[b_index]
        last = 'b'
        b_index -= 1
    else:
        return -1
    while True:
        if a_index == -1:
            return count + (last_value - b[b_index])
        elif b_index == -1:
            return count + (last_value - a[a_index])
        if a[a_index] > b[b_index]:
            count += (last_value - a[a_index])
            a_index -= 1
            last_value = a[a_index]
        elif a[a_index] < b[b_index]:
            count += (last_value - b[b_index])
            b_index -= 1
            last_value = b[b_index]
        else:
            return -1
    print a, b, count
    return count

quantity = int(raw_input())
dolls = [[doll] for doll in map(int, raw_input().split())]

count = 0

while True:
    index = -1
    min_diff = 999999
    for i in range(len(dolls)-1):
        diff = calculate_difference(dolls[i], dolls[i+1])
        #print diff,
        if diff == 1:
            index = i
            break
        if diff < min_diff and diff != -1:
            min_diff = diff
            index = i
    #print
    if index == -1:
        break
    final, tmp = merge(dolls[index], dolls[index+1])
    dolls.pop(index+1)
    dolls.pop(index)
    dolls.insert(index, final)
    count += tmp
    print dolls

possible = True
for doll in dolls:
    if not is_valid(doll):
        possible = False
        break

if possible:
    print count
else:
    print 'Impossible', count