def insert_child(actual, node, tree, refs):
    ref = refs[actual]
    if node < actual:
        if tree[ref][0] == None:
            tree[ref][0] = node
        else:
            insert_child(tree[ref][0], node, tree, refs)
    elif node > actual:
        if tree[ref][1] == None:
            tree[ref][1] = node
        else:
            insert_child(tree[ref][1], node, tree, refs)

cases = int(raw_input())

for i in range(cases):
    number_of_nodes = int(raw_input())
    nodes = map(int, raw_input().split())
    tree = [[None, None] for x in range(number_of_nodes)]
    position_pairs = {nodes[0] : 0}
    queue = [nodes[0]]
    k = 1
    for node in nodes[1:]:
        position_pairs[node] = k
        k += 1
        insert_child(nodes[0], node, tree, position_pairs)
    j = 0
    print "Case %d:" % (i+1)
    while j < number_of_nodes:
        actual = queue.pop(0)
        if j < number_of_nodes - 1:
            print actual, 
        else:
            print "%d\n" % actual
        for child in tree[position_pairs[actual]]:
            if child != None:
                queue.append(child)
        j += 1