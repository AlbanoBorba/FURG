def was_touched(position, indexes):
    for a, b in indexes:
        if a <= position <= b:
            return True
    return False

identifier = 1
while True:
    quantity = int(raw_input())
    if quantity == 0:
        break
    indexes = []
    genomes = range(quantity+1)
    swaps = int(raw_input())
    for i in xrange(swaps):
        a, b = map(int, raw_input().split())
        indexes.append((a, b))
        genomes = genomes[:a] + list(reversed(genomes[a:b+1])) + genomes[b+1:]
        #print genomes
    queries = int(raw_input())
    print "Genome %d" % identifier
    identifier += 1

    for i in xrange(queries):
        position = int(raw_input())
        if was_touched(position, indexes):
            print genomes.index(position)
        else:
            print position