queue = []


def enqueue():
    element = int(input("Enter the element:\n"))
    queue.insert(0, element)
    print(queue)


def dequeue():
    if not queue:
        print('Queue is empty')
    else:
        front_element = queue.pop()
        print("Element removed from front end is:\n", front_element)
        print(queue)


def isEmpty():
    if not queue:
        print("The queue is Empty.")


def isFull(n):
    if not queue:
        print("Queue is empty.")
    if len(queue) == n:
        print("Queue is Full.")
    else:
        print("Queue is not Full")


def getFrontElement():
    return queue[-1]


def getRearElement():
    return queue[0]


n = int(input("Enter the size of queue:"))
while n >= 0:
    enqueue()
    n = n - 1

while True:
    print("Choose any Operation:\n1. Dequeue \n2. Full \n3. Empty \n4. Get Front element \n5. Get Rear Element \n6. Exit")
    choice = int(input("Please enter your choice:\n"))
    if choice == 1:
        dequeue()
    elif choice == 2:
        isFull(n)
    elif choice == 3:
        isEmpty()
    elif choice == 4:
        ele = getFrontElement()
        print("Element at Front end is: ", ele)
    elif choice == 5:
        ele = getRearElement()
        print("Element at Rear end is: ", ele)
    else:
        break

