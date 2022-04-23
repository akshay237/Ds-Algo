stack = []


def push():
    element = input("Enter the element you want to insert:\n")
    stack.append(element)
    print(stack)


def pop_element():
    if not stack:
        print("Stack is empty.")
    else:
        element = stack.pop()
        print("Popped element is: ", element)
        print(stack)


def peek():
    if not stack:
        print("Stack is empty no element at top.")
    else:
        length = len(stack) - 1
        print("Topmost element of Stack is:\n", stack[length])


while True:
    print("You have these choice:\n 1.Push\n 2.Pop\n 3.Peek\n 4. Quit")
    print("Choose the choice from above:\n")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        peek()
    else:
        break
