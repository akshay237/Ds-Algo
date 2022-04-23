from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True

        # Recur for all the adjacent vertices of the current vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # If there are no adjacent vertices add that vertex to the stack
        stack.append(v)

    def topologicalSort(self):
        # create a visited array for all the nodes and initially add False for each vertex
        visited = [False]*self.V
        # create a empty stack to store the result
        stack = []

        # Check for all the vertices of graph
        for i in range(self.V):
            if (visited[i] == False):
                self.topologicalSortUtil(i, visited, stack)

        # print the stack in reverse order
        print(stack[::-1])


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Following is a Topological Sort of the given graph")

# Function Call
g.topologicalSort()