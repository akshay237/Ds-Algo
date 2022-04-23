def add_node(v):
    if v in graph:
        print(v, "is already present in the graph.")
    else:
        graph[v] = []


# for weighted graph we have to add the cost also, so we have to append a list that contains vertex and cost.
# list1 = [v2, cost], graph[v1].append(list1)
# list2 = [v1, cost], graph[v2].append(list2)
def add_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph.")
    elif v2 not in graph:
        print(v2, "is not present in the group.")
    else:
        # for directed graph there should be only one edge.
        graph[v1].append(v2)
        graph[v2].append(v1)


def delete_node(v):
    if v not in graph:
        print(v, "is not present in thr graph.")
    else:
        # pop the node from the dictionary
        graph.pop(v)
        # search the node in each value of the key and if present delete it.
        for k in graph:
            list1 = graph[k]
            if v in list1:
                list1.remove(v)


def delete_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph.")
    elif v2 not in graph:
        print(v2, "is not present in the graph.")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)


# Implementation of DFS using recursive approach
def DFS(v, visited, graph):
    if v not in graph:
        print("Node is not present in the graph.")
        return
    if v not in visited:
        print(v)
        visited.add(v)
        for i in graph[v]:
            DFS(i, visited, graph)



# DFS using iterative approach
# def DFSIterative(v, graph):
#     visited = set()
#     if v not in graph:
#         print("Node is not present in the graph.")
#         return
#     stack = []
#     stack.append(v)
#     # we have to follow the below steps untill stack is not empty so putted a for loop.
#     while stack:
#         curr = stack.pop()
#         if curr not in visited:
#             print(curr)
#             visited.add(curr)
#             for i in graph[curr]:
#                 stack.append(i)


def BFS(v, graph):
    visited = set()
    if v not in graph:
        print(v, "node is not present in the graph.")
        return
    queue = []
    queue.append(v)
    while queue:
        curr = queue.pop(0)
        if curr not in visited:
            print(curr)
            visited.add(curr)
            for i in graph[curr]:
                queue.append(i)



graph = {}
# uncomment visited if you are calling DFS recursive function
visited = set()
add_node('A')
add_node('B')
add_node('C')
add_node('D')
print("Before adding the edges the graph is: ")
print(graph)
add_edge('A', 'B')
add_edge('A', 'C')
add_edge('B', 'C')
add_edge('C', 'D')
add_edge('D', 'D')
print("After adding the edges the graph is: ")
print(graph)
print("DFS traversal of the graph is: ")
DFS('C', visited, graph)
# print("DFS traversal using iterative approach:")
# DFSIterative('C', graph)
print("BFS traversal of the graph is: ")
BFS('C', graph)
print("After deleting the edges from node D graph is: ")
delete_edge('B', 'D')
print(graph)
print("After deleting the node D from graph is: ")
delete_node('D')
print(graph)