# Reverse a String: HI, My name is Akshay
# Output : yahskA si eman yM ,IH
import array


def ReverseString(string):
    if len(string) <= 1:
        return "Please provide a valid String"
    arr = array.array('u', [])
    length = len(string) - 1
    while length >= 0:
        arr.append(string[length])
        length = length - 1
    myList = arr.tolist()
    return myList


string = "Hey My Name is Akshay"
myStr = ReverseString(string)
string = ""
print(string.join(myStr))
