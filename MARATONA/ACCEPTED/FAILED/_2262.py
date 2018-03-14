top = 0

def is_valid(thingy):
    if thingy[0] != 1:
        return False
    for i in range(len(thingy)-1):
        if thingy[i+1] - thingy[i] != 1:
            return False
    return True

def merge_two(a, b):
    ai = len(a)-1
    bi = len(b)-1
    one = []
    opens = 0
    while True:
        if ai == -1:
            one = b[:bi+1] + one
            #opens += 1
            break
        elif bi == -1:
            one = a[:ai+1] + one
            #opens += 1
            break
        elif a[ai] > b[bi]:
            one.insert(0, a[ai])
            ai -= 1
            opens += 1
        elif a[ai] < b[bi]:
            one.insert(0, b[bi])
            bi -= 1
            opens += 1
        else:
            return None, None
    return one, opens

def merge(thingy, i):
    new_list = list(thingy)
    tmp, cnt = merge_two(new_list[i], new_list.pop(i+1))
    if tmp == None:
        return None, None
    new_list[i] = tmp
    return new_list, cnt

def combine(thingy, count):
    global top
    result = []
    possibilities = []
    for i in range(len(thingy)-1):
        top += 1
        try:
            tmp, cnt = merge(thingy, i)
            if tmp == None:
                break
            cnt += count
        except IndexError:
            break
        possible = True
        for doll in tmp:
            if not is_valid(doll):
                possible = False
                break
        possibilities.append((tmp, cnt))
    for p, count in possibilities:
        result.append(combine(p, count))
    return result
    

quantity = int(raw_input())
dolls = [[x] for x in map(int, raw_input().split())]

print combine(dolls, 0)
print top