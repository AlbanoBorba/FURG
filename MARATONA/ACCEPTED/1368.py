def hori(cube):
    aux = list(cube)
    cube[0] = aux[2]
    cube[2] = aux[5]
    cube[4] = aux[0]
    cube[5] = aux[4]

def vert(cube):
    aux = list(cube)
    cube[1] = aux[4]
    cube[2] = aux[1]
    cube[3] = aux[2]
    cube[4] = aux[3]

def on_axis(cube):
    aux = list(cube)
    cube[0] = aux[5]
    cube[1] = aux[3]
    cube[3] = aux[1]
    cube[5] = aux[0]

def compare_cubes(a, b):
    if sorted(a) != sorted(b):
        return False
    for i in xrange(5):
        if a == b:
            return True
        for j in xrange(5):
            for k in xrange(5):
                on_axis(a)
                if a == b:
                    return True
            on_axis(a)
            vert(a)
            if a == b:
                return True
        hori(a)
    return False

while True:
    quantity = int(raw_input())
    if quantity == 0:
        break
    cubes = []
    for k in xrange(quantity):
        cube = [int(raw_input())]
        cube += map(int, raw_input().split())
        cube.append(int(raw_input()))
        cubes.append(cube)
    groups = [cubes[0]]
    for cube in cubes[1:]:
        found = False
        for group in groups:
            if compare_cubes(cube, group):
                found = True
                break
        if not found:
            groups.append(cube)
    print len(groups)