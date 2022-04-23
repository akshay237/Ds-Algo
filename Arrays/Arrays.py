arrayofNumbers = [1, 2, 3, 4, 5]
print(arrayofNumbers)


def findElement(array):
   length = len(array)
   for i in range(length):
      if(array[i] == 3):
          print("Element Found")
          break



def findPairs(array):
    for i in range(len(array)):   # O(n)
        # j = i+1
        for j in range(len(array)):  # O(n) 
            print(array[i], array[j])


findElement(arrayofNumbers)
findPairs(arrayofNumbers)