nodes = []
graph = []
node_count = 0


def add_node(v):
    if v in nodes:
        print(v, "is already present in the graph.")
        return
    else:
        global node_count
        node_count = node_count + 1
        nodes.append(v)
        # We will add the extra column so each row is a list and will append a zero to each row, so it will be added
        # in the last of each row.
        for n in graph:
            n.append(0)
        temp = []
        temp = [0]*node_count
        # We will add the extra row here.
        graph.append(temp)


def add_edge(v1, v2):
    if v1 not in nodes:
        print(v1, "node is not present in the graph")
    elif v2 not in nodes:
        print(v2, "node is not present in the graph.")
    else:
        idx1 = nodes.index(v1)
        idx2 = nodes.index(v2)
        graph[idx1][idx2] = 1
        graph[idx2][idx1] = 1

def delete_node(v):
    if v not in nodes:
        print(v, "is not present in the graph.")
    else:
        # find the index of node that have to be removed, decrement the node_count counter and remove the node from nodes list.
        idx = nodes.index(v)
        global node_count
        node_count -= 1
        nodes.remove(v)
        # Delete the row of the node which have to delete from the adjaceny matrix.
        graph.pop(idx)
        # Delete the column for that we have to iterate using a loop and from every row remove the value from the idx.
        # Because the matrix is a list of nested lists row wise.
        for i in graph:
            i.pop(idx)


def delete_edge(v1, v2):
    if v1 not in nodes:
        print(v1, " is not present in the graph.")
    elif v2 not in nodes:
        print(v2, " is not present in the graph.")
    else:
        idx1 = nodes.index(v1)
        idx2 = nodes.index(v2)
        graph[idx1][idx2] = 0
        graph[idx2][idx1] = 0


def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()


print("Before adding nodes:")
print(nodes)
print(graph)
add_node('A')
add_node('B')
add_node('C')
add_node('D')

print("After adding nodes:")
print(nodes)
print(graph)
add_edge("A", "D")
add_edge("A", "C")
add_edge('B', 'C')
add_edge('A', 'B')
print_graph()

print("Delete the Edges from node D")
delete_edge('A', 'D')
delete_node('D')
print("The graph is : ")
print_graph()