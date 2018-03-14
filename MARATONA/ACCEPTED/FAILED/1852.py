sun = int(raw_input())
wanting_dict = {}
people = []
direwolfs = []

for i in xrange(sun):
    person, order = raw_input().split(" ", 1)
    people.append(person)
    wanting_dict[person] = order.split()

for i in xrange(sun):
    direwolf, order = raw_input().split(" ", 1)
    direwolfs.append(direwolf)
    wanting_dict[direwolf] = order.split()

owned = []


pm = [[0 for j in xrange(sun)] for i in xrange(sun)]
dm = [[0 for j in xrange(sun)] for i in xrange(sun)]

owners = []
chosen = []
leave = False
for i in xrange(sun*2):
    if leave:
        break
    for person in people:
        if leave:
            break
        for direwolf in direwolfs:
            if leave:
                break
            pw, dw = wanting_dict[person].index(direwolf), wanting_dict[direwolf].index(person)
            if pw+dw == i and direwolf not in chosen and person not in owners:
                print person, direwolf, pw + dw
                owners.append(person)
                chosen.append(direwolf)
                if len(owners) == sun:
                    leave = True

for i in xrange(sun):
    print owners[i], chosen[i]