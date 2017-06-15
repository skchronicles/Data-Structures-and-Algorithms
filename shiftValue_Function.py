#Skyler Kuhn
#Quiz I: Problem 1
#Create a function that shifts the contents of a List X units to the right.
#The function should take in a List and a shift value as a argument.


def shiftValue_List(arr, shift):
    if shift >= 0:
        to_return = [None] * len(arr)
        for k in range(len(arr)):
            j = k + (shift) % len(arr)
            to_return[k] = arr[j]
        return to_return
    else:
        print("Please enter a non-negative integer as a shift parameter")
 
a = [22,-6,0,-84,39,9,-1]

shiftValue_List(a, 3)
shiftValue_List(a, 1)
l = shiftValue_List(a, -5)
print(l)