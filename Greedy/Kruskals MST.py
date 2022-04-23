from collections import  defaultdict


class Graph:
    def __init__(self, Vertices):
        self.V = Vertices
        self.graph = []

    # Add the edges to the graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # It will find the parent of node with edge have to be connected.
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        # Attach the smaller rank tree under the high rank tree
        # Basically this logic will help in detecting the cycle.
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[yroot] < rank[xroot]:
            parent[yroot] = xroot
        # if rank is same made one as root and increment the rank
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskalMST(self):
        res = []   # stores the edges with weight
        i = 0  # index variable used for sorted array
        e = 0  # index variable used for result list

        # sort the graph on the basis of weight
        self.graph.sort(key=lambda x: x[2])

        parent = []
        rank = []

        # add each node to parent and rank for each node should be zero
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        # checking all the edges untill we have v-1 edges in the result.
        while e < self.V - 1:
            # pick the smallest edge and check whether it contains cycle or not if not than add it to MST.
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            # if the nodes are not same than these are not part of same sub graph so we can add them to result
            if x != y:
                res.append([u, v, w])
                e = e + 1
                self.union(parent, rank, x, y)

        minimumCost = 0
        print("Edges in the constructed MST:")
        for u, v, weight in res:
            minimumCost += weight
            print("%d ---> %d ==> %d" % (u, v, weight))
        print("Minimum Spanning Tree:", minimumCost)


g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

# Function call
g.kruskalMST()