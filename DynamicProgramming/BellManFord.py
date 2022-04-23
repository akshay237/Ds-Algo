class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printGraph(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellmanFord(self, source):
        # Initially assign infinite distance to each vertex
        dist = [float("Inf")] * self.V
        # shortest distance from source to source is 0
        dist[source] = 0
        # This step will calculate the shortest distance for each of the vertex
        for _ in range(self.V - 1):
            # check for each edge combination
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # This step will check whether the graph contain any negative edge or not
        # Again do one more iteration of above step
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle.")
                return

        # print the graph containing shortest distance
        self.printGraph(dist)


g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

g.bellmanFord(0)
