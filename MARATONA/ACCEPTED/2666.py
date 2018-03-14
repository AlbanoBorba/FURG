import math
import sys

sys.setrecursionlimit(100000)

kilometers = 0

class Node:
    def __init__(self, identifier, dist, gold):
        self.identifier = identifier
        self.dist = dist
        self.gold = gold
        self.children = []
    
    def return_parent(self, origin, destination, distance):
        if self.identifier == origin:
            return self, destination
        elif self.identifier == destination:
            return self, origin
        else:
            for child in self.children:
                found = child.return_parent(origin, destination, distance)
                if found != None:
                    return found

    def retrieve_gold(self, cap):
        global kilometers
        for child in self.children:
            child.retrieve_gold(cap)
            kilometers += int(math.ceil(float(child.gold)/float(cap))*2*child.dist)
            self.gold += child.gold
            child.gold = 0

"""
def retrieve_gold(tree, capacity, node, last, money_owed):
    global kilometers
    for identifier, distance in tree[node]:
        if identifier != last:
            retrieve_gold(tree, capacity, identifier, node, money_owed)
            trips = math.ceil(float(money_owed[identifier-1])/capacity)
            kilometers += 2*distance*int(trips)
            money_owed[node-1] += money_owed[identifier-1]
            money_owed[identifier-1] = 0
"""
def main():
    cities, capacity = map(int, raw_input().split())
    money_owed = map(int, raw_input().split())

    capitol = Node(1, 0, money_owed[0])
    """
    tree = [[] for x in range(cities+10)]

    for i in range(cities-1):
        origin, destination, distance = map(int, raw_input().split())
        tree[origin].append((destination, distance))
        tree[destination].append((origin, distance))
    
    retrieve_gold(tree, capacity, 1, None, money_owed)

    """
    for i in range(cities-1):
        origin, destination, distance = map(int, raw_input().split())
        parent, identifier = capitol.return_parent(origin, destination, distance)
        parent.children.append(Node(identifier, distance, money_owed[identifier-1]))

    capitol.retrieve_gold(capacity)

    print kilometers

main()