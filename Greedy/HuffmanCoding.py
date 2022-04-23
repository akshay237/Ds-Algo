class Node:
    # initialize the frequency, symbol and huffman code for each node
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''


# print the huffman code for each character
def printCodes(node, val=''):
    # code for the current node
    newVal = val + str(node.huff)

    # if tree have left and right child
    if node.left:
        printCodes(node.left, newVal)
    if node.right:
        printCodes(node.right, newVal)

    # when we encounter the leaf node print the value of newVal
    if (not node.left) and (not node.right):
        print(f"{node.symbol} ---> {newVal}")


freq = [5, 9, 12, 13, 16, 45]
chars = ['a', 'b', 'c', 'd', 'e', 'f']
nodes = []

for node in range(len(freq)):
    nodes.append(Node(freq[node], chars[node]))

# iterate through the heap untill it have only one node
while len(nodes) > 1:
    # sort the nodes list in ascending order of frequency
    nodes = sorted(nodes, key=lambda x: x.freq)
    # take the first minimum node as left
    left = nodes[0]
    # take the second minimum node as right
    right = nodes[1]

    # assign the huffman code to the left and right node as
    left.huff = 0
    right.huff = 1

    # make a new node with the sum of two minimum node and removes the two node and add the new to the tree
    newNode = Node(left.freq+right.freq, left.symbol+right.symbol, left, right)

    # remove the left and right node and append the new Node
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)


print("\nThe Huffman Code for each of node of huffman tree is: ")
printCodes(nodes[0])
