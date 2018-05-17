while True:
    quantity = int(raw_input())
    if quantity == 0:
        break
    connections = {}
    origins = []
    destinies = []
    function = True
    invertible = True
    for num in xrange(quantity):
        origin, destiny = raw_input().split(" -> ")
        if origin in origins:
            invertible = False
        if destiny in destinies:
            invertible = False
        origins.append(origin)
        destinies.append(destiny)
        if origin in connections.keys():
            connections[origin].append(destiny)
        else:
            connections[origin] = [destiny]
    
    for key, thingy in connections.items():
        if len(thingy) > 1:
            function = False
    #print connections


    if function:
        if invertible:
            print "Invertible."
        else:
            print "Not invertible."
    else:
        print "Not a function."
