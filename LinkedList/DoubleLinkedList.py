class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Traversing the whole linked list and printing it's data
    def printList(self):
        n = self.head
        if n is None:
            print("Linked List is empty.")
        else:
            while n is not None:
                print(n.data, end="<--->")
                n = n.right

    def printReverseTraversal(self):
        n = self.head
        if n is None:
            return 'Linked List is empty'
        while n.right is not None:
            n = n.right
        while n is not None:
            print(n.data, end='<-->')
            n = n.left

    # When we have to insert at first we have to check first whether the list is empty or not
    # If empty than assign head to new node
    # If not empty than assign new_node right to head and head's left to new node and head is new node
    def insertAtFirst(self, data):
        new_node = Node(data)
        n = self.head
        if n is None:
            self.head = new_node
        else:
            new_node.right = n
            n.left = new_node
            self.head = new_node

    # When we have to insert at End traverse till the end of list
    # After reaching last node's right is new_node and new_node's left is last node
    def insertAtEnd(self, data):
        new_node = Node(data)
        n = self.head
        if n is None:
            self.head = new_node
        while n.right is not None:
            n = n.right
        n.right = new_node
        new_node.left = n

    # When we have to insert after a node we have to traverse the list untill we find the node
    # After finding we change the current node right to new node right and current right will be new node
    # Before assigning we have make current's right left link will be new node and new node left will be current
    def insertAfterNode(self, data, value):
        n = self.head
        while n is not None:
            if n.data == value:
                break
            n = n.right

        if n is None:
            print("Value not found in linked list after which current node have to insert")
        else:
            new_node = Node(data)
            new_node.right = n.right
            new_node.left = n
            if n.right is not None:
                n.right.left = new_node
            n.right = new_node

    # When we have to insert before a node we need a previous to store previous link
    # When the node is found store the previous and change new_node.right now will be previous.right.
    # And current.left will be new_node, prev.right will be current and new_node left will be prev node.
    def insertBeforeNode(self, data, value):
        new_node = Node(data)
        prev = None
        n = self.head
        if n.data == value:
            new_node.right = n
            n.left = new_node
            self.head = new_node
            return

        while n is not None:
            if n.data == value:
                break
            prev = n
            # n.left = prev
            n = n.right

        if n is None:
            print("Value not found in linked list after which current node have to insert")
        else:
            new_node.right = prev.right
            # n.left = new_node
            prev.right = new_node
            new_node.left = prev

    def deleteFromFirst(self):
        n = self.head
        if n is None:
            print("Linked List is empty")
        # If there is only one element in the list
        elif n.right is None:
            self.head = None
        else:
            self.head = n.right
            self.head.left = None

    def deleteFromEnd(self):
        n = self.head
        prev = None
        # If there are no nodes
        if n is None:
            print("Linked list is empty.")
            return
        # If there is only one element in list
        if n.left is None and n.right is None:
            self.head = None
            return
        while n.right is not None:
            prev = n
            n = n.right
        prev.right = None

    # def deleteAnyNode(self, value):
    #     n = self.head
    #     prev = None
    #     # If linked list is empty
    #     if n is None:
    #         return "Linked List is empty"
    #     # If node value matches to head
    #     if self.head.data == value:
    #         # Only one node
    #         if self.head.right is None:
    #             self.head = None
    #         # Other nodes also there
    #         else:
    #             self.head = self.head.right
    #             self.head.left = None
    #         return
    #     while n is not None:
    #         if n.data == value:
    #             break
    #         prev = n
    #         n = n.right
    #
    #     if n is None:
    #         print("Value does not match in the linked list or Link list is empty")
    #     prev.right = n.right
    #     # If it is last node than no need to set the left
    #     if n.right is not None:
    #         n.right.left = prev

    def deleteAnyNode(self, value):
        n = self.head
        prev = None
        # No elements in linked list
        if n is None:
            return "Linked List is empty."
        # If value matches to first element
        if n.data == value:
            # Only One Node
            if n.right is None:
                self.head = None
            # After first element other elements are also there
            else:
                self.head = n.right
                self.head.left = None
        while n.right is not None:
            if n.data == value:
                break
            prev = n
            n = n.right
        # If value matches with middle nodes
        if n.right is not None:
            prev.right = n.right
            n.right.left = prev
        # If it is last Node
        if n.right is None:
            if n.data == value:
                prev.right = None
            else:
                return "Linked List does not contain the element you want to delete."

link = LinkedList()
link.insertAtFirst(10)
link.insertAtFirst(5)
link.insertAtFirst(2)
link.insertAtEnd(15)
link.insertAtEnd(30)
link.printList()
link.insertAfterNode(20, 15)
link.insertAfterNode(35, 30)
print('\nInserting after a node')
link.printList()
link.insertBeforeNode(12, 15)
link.insertBeforeNode(1, 2)
print('\nInserting Before a node')
link.printList()
link.deleteFromFirst()
print("\nAfter removing first element from start:")
link.printList()
link.deleteFromEnd()
print("\nDeleting element from last of linked list")
link.printList()
print('\nDeleting node with value from linked list')
link.deleteAnyNode(12)
link.printList()
print('\nLinked List print in reversal order')
link.printReverseTraversal()