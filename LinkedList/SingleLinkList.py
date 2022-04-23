class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Traversal through a link list
    def printLinkedList(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data, end="-->")
                n = n.next

    # Insert at Beginning we have to do
    # Create a new node first
    # Point the next of new node to head
    # Change head as new node
    def insertAtFirst(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    # Insert at End
    # Traversal till last node
    # Change next of last node to new node
    def insertAtEnd(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = node

    # When insert node in between
    # We need to store previous node when it matches the data of current node
    # Point the next of previous node to new node and next of new node to current node
    def insertBetween(self, data, key):
        new_node = Node(data)
        prev = None
        n = self.head
        while n.next is not None and n.data != key:
            prev = n
            n = n.next
        prev.next = new_node
        new_node.next = n

    # When we have to insert a node after a node
    # We have to find the node first after which we have to insert new node
    # Change the next of new node to current node's next and current node's next to new node
    def insertAfterNode(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("Node is not present in the linked list.")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    # When delete node from end
    # Check whether link list is already empty or not
    # If not then change the head to next node
    def deleteAtFirst(self):
        n = self.head
        if n is None:
            print("Linked List is empty so can not delete.")
        else:
            self.head = n.next

    # When delete node from last
    # We need a prev node to store the previous node when reaches the end
    # Change the next of prev node to None
    def deleteAtEnd(self):
        n = self.head
        prev = None
        if n is None:
            print("Linked List is already empty.")
        while n.next is not None:
            prev = n
            n = n.next
        prev.next = None

    # When delete any node we have to find the node which have to be deleted
    # Once the value is find use a prev variable and change the link of prev's next to current's next
    def deleteAnyNode(self, val):
        n = self.head
        prev = None
        while n.next is not None and n.data != val:
            prev = n
            n = n.next
        prev.next = n.next


link = LinkedList()
link.insertAtFirst(10)
link.insertAtFirst(5)
link.insertAtEnd(25)
link.insertAtEnd(30)
link.insertAtFirst(3)
print("Elements of linked list are:")
link.printLinkedList()
link.insertBetween(15, 25)
link.insertBetween(20, 25)
print("\nElement of Linked List when inserting in between:")
link.printLinkedList()
link.deleteAtFirst()
print("\nAfter deleting first element of link list:")
link.printLinkedList()
link.deleteAtEnd()
print("\nLinked List after deleting last element:")
link.printLinkedList()
link.deleteAnyNode(20)
print("\nAfter deleting specific Node:")
link.printLinkedList()
link.insertAfterNode(21, 15)
print("\nInserting new node after a  Node:")
link.printLinkedList()