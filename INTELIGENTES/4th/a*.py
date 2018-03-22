class Node:
    def __init__(self, identifier, heuristic):
        self.identifier = identifier
        self.heuristic = heuristic
        self.edges = []

    def add_edge(self, destiny, size):
        self.edges.append(Edge(destiny, size))

class Edge:
    def __init__(self, target, size):
        self.size = size
        self.target = target

def a_star(origin, destiny, visited):
    visited.append(origin.identifier)
    

def main():
    graph = {}
    nodes = int(raw_input("Digite o numero de nodos no grafo"))
    print ("Informe os nodos e suas heuristicas")
    for i in range(nodes):
        node_name, heuristic = raw_input().split())
        graph[node_name] = (Node(node_name, int(heuristic)))
    edges = int(raw_input("Digite o numero de vertices no grafo"))
    print ("Infome os vertices")
    for i in range(edges):
        origin, destiny, size = raw_input().split()
        graph[origin].add_edge(graph[destiny], int(size))
        graph[destiny].add_edge(graph[origin], int(size))
        
    