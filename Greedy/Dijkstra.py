import sys

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [0 for c in range(self.V) for r in range(self.V)]

    def printGraph(self, dist, parent):
        print("Distance of each vertex from the source node is: ")
        print('Vertex \t Distance from Source')
        for v in range(self.V):
            print(v, '\t\t\t', dist[v])
        print('The constructed graph using Dijkstra is below')
        for v in range(self.V):
            print(v, "------->", parent[v])

    # function to find the minimum distance from source node  for a vertex which is not included in sptSet
    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        # iterate through whole row and find the minimum and return the index
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_idx = u
        return min_idx

    def dijkstra(self, source):
        # dist array to store the distance from the source to each vertex.
        dist = [sys.maxsize] * self.V
        # distance of source to source is 0
        dist[source] = 0
        # shortest path set contains vertices which have minimum distance from source to given vertex
        sptSet = [False] * self.V
        # Parent array which contains the parent node for each vertex and help in printing each edge
        parent = [None] * self.V
        parent[source] = -1
        # pick the minimum distance vertex from the set of vertices which are not yet processed.
        for i in range(self.V):
            u = self.minDistance(dist, sptSet)
            # Including the vertex in the shortest path first list
            sptSet[u] = True
            # for the adjacent vertices of u have minimum distance from source and not included in sptSet.
            for v in range(self.V):
                 if (self.graph[u][v] > 0) and (sptSet[v] == False) and (dist[u] + self.graph[u][v] < dist[v]):
                     dist[v] = dist[u] + self.graph[u][v]
                     parent[u] = v
        # print the result once graph is iterated
        self.printGraph(dist, parent)


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ];

g.dijkstra(0);


