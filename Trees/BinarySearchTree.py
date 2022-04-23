class BST:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

    def insert(self, data):
        # if tree is empty
        if self.key is None:
            self.key = data
            return
        # if tree not empty and value less than root
        if self.key >= data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        # if tree is not empty and value is greater than root value
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)

    def search(self, data):
        # if tree is empty
        if self.key is None:
            return " Tree is empty we can't search."
        # if not empty and the search value is equal to root node key
        if self.key == data:
            print("Given value is found.")
            return
        # if not equal to root key and the searched value is less than root's key
        if self.key >= data:
            if self.left:
                self.left.search(data)
            else:
                print("Searched Value is not there in tree.")
                return
        # if search value is greater than root's key
        else:
            if self.right:
                self.right.search(data)
            else:
                print("Searched Value is not there in tree.")
                return

    # In pre-order traversal root node first than left node and then right node
    def preorder(self):
        if self.key is not None:
            print(self.key)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
        if self.key is None:
            print("Tree is Empty.")
            return

    # In in-order traversal left node first then root node and then right node.
    def inorder(self):
        if self.key is None:
            print("Tree is empty.")
            return
        if self.key is not None:
            if self.left:
                self.left.inorder()
            print(self.key)
            if self.right:
                self.right.inorder()

    # In post-order traversal first right node then left node and in the end root node is traversed.
    def postorder(self):
        if self.key is None:
            print("Tree is Empty.")
            return
        if self.key is not None:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.key)

    def delete(self, data, curr):
        # if tree is empty
        if self.key is None:
            print("Tree is empty so delete operation can not be performed.")
            return
        # if given node less than root key
        if data < self.key:
            if self.left:
                self.left = self.left.delete(data, curr)
            else:
                print("Given node is not present in Tree.")
        # if given node is greater than root node's key
        elif data > self.key:
            if self.right:
                self.right = self.right.delete(data, curr)
            else:
                print("Given node is not present in Tree.")
        else:
            # Condition for node have zero or one child
            if self.left is None:
                temp = self.right
                # Check whether the node have to delete is root node and have right child only
                if data == curr:
                    self.key = temp.key
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    return
                self = None
                return temp
            if self.right is None:
                temp = self.left
                # Check whether the node have to delete is root node and have left child only
                if data == curr:
                    self.key = temp.key
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    return
                self = None
                return temp
            # if node have both the child
            node = self.right
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.delete(node.key, curr)
        return self

    def min_node(self):
        curr = self
        if curr is not None:
            while curr.left:
                curr = curr.left
            print("Node with the smallest value is : ", curr.key)

    def max_node(self):
        curr = self
        if curr is not None:
            while curr.right:
                curr = curr.right
            print("Node with the highest value is : ", curr.key)


def count_nodes(node):
    if node is None:
        return 0
    else:
        return 1 + count_nodes(node.left) + count_nodes(node.right)


root = BST(5)
values = [2, 4, 12, 9, 15, 1]
for i in values:
    root.insert(i)
search = root.search(15)
print("No of nodes are: ", count_nodes(root))
print(search)
root1 = BST(None)
print("Pre-order Traversal is:")
root.preorder()
print("In-order Traversal is:")
root.inorder()
print("Post-order Traversal is:")
root.postorder()
root.min_node()
root.max_node()
if count_nodes(root) > 1:
    root.delete(5, root.key)
else:
    print("Delete operation can not be performed.")
print("In-order Traversal after deleting root node is:")
root.inorder()