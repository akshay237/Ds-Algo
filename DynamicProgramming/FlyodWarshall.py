V = 4
INF = 9999


def flyod(graph):
    # initialize the dist[][] matrix same as the input matrix and then we do the changes in the dist matrix by
    # updating the distance
    dist = list(map(lambda x: list(map(lambda y: y, x)), graph))

    # k is the intermediate vertex
    for k in range(V):
        # i is the source vertex
        for i in range(V):
            # j is the destination vertex in the graph
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # print the graph
    printSolution(dist)

def printSolution(dist):
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print(' %7s' % ("INF"), end="")
            else:
                print('%7d\t' % (dist[i][j]), end="")
            if j == V-1:
                print()


graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]

print("The shortest distance between all pairs of vertices are:")
flyod(graph)
