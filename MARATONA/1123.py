# Python program for Dijkstra's single 
# source shortest path algorithm. The program is 
# for adjacency matrix representation of the graph
 
# Library for INT_MAX
import struct
#max_int = 2 ** (struct.Struct('i').size * 8 - 1) - 1
max_int = 1061109567

class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]
 
    # A utility function to find the vertex with 
    # minimum distance value, from the set of vertices 
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initilaize minimum distance for next node
        minimum = max_int
        # Search not nearest vertex not in the 
        # shortest path tree
        for v in range(self.V):
            if dist[v] <= minimum and sptSet[v] == False:
                minimum = dist[v]
                minimum_index = v
        #print (dist, self.V)
        return minimum_index
 
    # Funtion that implements Dijkstra's single source 
    # shortest path algorithm for a graph represented 
    # using adjacency matrix representation
    def dijkstra(self, src, C):
 
        dist = [max_int] * self.V
        #print (dist, src)
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from 
            # the set of vertices not yet processed. 
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the 
            # shotest path tree
            sptSet[u] = True
 
            # Update dist value of the adjacent vertices 
            # of the picked vertex only if the current 
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            print (dist, sptSet, u)
            if u < C:
                if sptSet[u+1] == False and dist[u+1] > dist[u] \
                                            + self.graph[u][u+1]:
                    dist[u+1] = dist[u] + self.graph[u][u+1]
            else:
                for v in range(self.V):
                    if self.graph[u][v] > 0 and sptSet[v] == False and \
                    dist[v] > dist[u] + self.graph[u][v]:
                            dist[v] = dist[u] + self.graph[u][v]
 
        return dist

while True:
    N, M, C, K = map(int, input().split())
    if N == 0 and M == 0 and C == 0 and K == 0:
        break
    g  = Graph(N)
    g.graph = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        ori, dst, dist = map(int, input().split())
        g.graph[ori][dst] = dist
        g.graph[dst][ori] = dist
        #fill_matrix(g.graph, ori, dst, dist, C)
    dist = g.dijkstra(K, C);
    print (dist[C-1])

# This code is contributed by Divyanshu Mehta