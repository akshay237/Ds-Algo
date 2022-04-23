import sys

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for c in range(vertices)] for r in range(vertices)]

    def printMST(self, parent):
        print("The constructed MST using prim's Algorithm:")
        print('Edge \t\tWeight')
        for i in range(1, self.V):
            print(parent[i], "--->", i, "\t", self.graph[i][parent[i]])

    # function to find vertex with minimum distance value from set of vertices and not included in mstSet
    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_idx = v
        return min_idx

    # function to construct MST and print MST for a graph
    def primMST(self):
        # key value used to pick minimum weight
        key = [sys.maxsize] * self.V
        # parent used to store the constructed MST
        parent = [None] * self.V
        # Always pick the first vertex
        key[0] = 0
        # There is no parent for root node
        parent[0] = -1
        # mstSet has track of vertex which are visited or not
        mstSet = [False] * self.V
        # iterate through the whole graph
        for i in range(self.V):
            # pick the minimum distance vertex from the set of vertices that are not processed yet.
            u = self.minKey(key, mstSet)
            # After selecting add it into mstSet
            mstSet[u] = True

            for v in range(self.V):
                # graph[u][v] is non-zero for adjacent vertices of m, mstSet[v] is false for not included vertices
                # Update the key only if graph[u][v] is smaller than key[v]
                if (self.graph[u][v] > 0) and (mstSet[v] == False) and (self.graph[u][v] < key[v]):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

g.primMST()

