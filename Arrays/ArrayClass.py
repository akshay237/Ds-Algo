import array


class MyArray:
    def __init__(self,  data):
        self.data = data

    def getElement(self, index):
        return self.data[index]

    def addElement(self, value):
        self.data.append(value)

    def removeElement(self):
        self.data.pop()

    def printArray(self):
        for i in range(len(self.data)):
            print(self.data[i])

    def length(self):
        return len(self.data)

    def insertAt(self, index, value):
        self.data.insert(index, value)

    def reverseArray(self):
        self.data.reverse()


data = array.array('i', [])
arr = MyArray(data)
arr.addElement(5)
arr.addElement(10)
arr.addElement(15)
arr.addElement(20)
print("Elements of Array are: ")
arr.printArray()

length = arr.length()
print("Length of Array is: ", length)
lastValue = arr.getElement(length - 1)
print("Last Value is: ", lastValue)

arr.removeElement()
print("After removing last element:")
arr.printArray()

print("Inserting element in 2nd position: ")
arr.insertAt(1, 25)
arr.printArray()

print("Reverse the content of array: ")
arr.reverseArray()
arr.printArray()