###############################################################
#Group: Millington
#Project I: A Battle of Sorts
#Create an insertion sort function and a selection sort function
################################################################
import time
import random
#############

#Insertion Sort Function
def insertion_sort(arr):
    for k in range(1, len(arr)):
        item_to_place = arr[k]
        j = k
        while j > 0 and arr[j-1] > item_to_place:
            arr[j] = arr[j-1]
            j = j-1 
        arr[j] = item_to_place

#Selection Sort Function:
def selection_sort(arr):
    for k in range(0,len(arr)-1):
        minIndex = k
        for j in range(k+1,len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if minIndex != k:
            arr[k], arr[minIndex] = arr[minIndex], arr[k]

####################################
#Lists used for Performance Testing:
## Sorted Increasing List 
sorted_Increasing1000 = []
sorted_Increasing2500 = []
sorted_Increasing5000 = []
sorted_Increasing7500 = []
sorted_Increasing10000 = []
for k in range(1,1001):
    sorted_Increasing1000.append(k)
for k in range(1,2501):
    sorted_Increasing2500.append(k)
for k in range(1,5001):
    sorted_Increasing5000.append(k)
for k in range(1,7501):
    sorted_Increasing7500.append(k)
for k in range(1,10001):
    sorted_Increasing10000.append(k)

## Sorted Decreasing List
sorted_Decreasing1000 = []
sorted_Decreasing2500 = []
sorted_Decreasing5000 = []
sorted_Decreasing7500 = []
sorted_Decreasing10000 = []
for k in range(1000,0,-1):
    sorted_Decreasing1000.append(k)
for k in range(2500,0,-1):
    sorted_Decreasing2500.append(k)
for k in range(5000,0,-1):
    sorted_Decreasing5000.append(k)
for k in range(7500,0,-1):
    sorted_Decreasing7500.append(k)
for k in range(10000,0,-1):
    sorted_Decreasing10000.append(k)

## Sorted Random List
random_ValuesList1000 = []
random_ValuesList2500 = []
random_ValuesList5000 = []
random_ValuesList7500 = []
random_ValuesList10000 = []
for k in range(1000):
    random_ValuesList1000.append(random.randint(1,1001))
random_ValuesList2_1000 = random_ValuesList1000[:]
for k in range(2500):
    random_ValuesList2500.append(random.randint(1,2501))
random_ValuesList2_2500 = random_ValuesList2500[:]
for k in range(5000):
    random_ValuesList5000.append(random.randint(1,5001))
random_ValuesList2_5000 = random_ValuesList5000[:]
for k in range(7500):
    random_ValuesList7500.append(random.randint(1,7501))
random_ValuesList2_7500 = random_ValuesList7500[:]
for k in range(10000):
    random_ValuesList10000.append(random.randint(1,10001))
random_ValuesList2_10000 = random_ValuesList10000[:] #making another copy to pass to the other funct  


##############################
#Testing Function Performance:
#Timing the Sorted Increasing List with the two functions:
##1000 Insertion Sort Fucntion
print "   "
print"Testing the Performance of the Insertion and Selection Sorting Functions:"
print "##################################################################"
start = time.clock() 
insertion_sort(sorted_Increasing1000)
end = time.clock()
print "1000 Increasing Insertion: " + "{:.20f}".format(end-start)
##1000 Selection Sort Function                                                   
start = time.clock()
selection_sort(sorted_Increasing1000)
end = time.clock()
print "1000 Increasing Selection: " + "{:20f}".format(end-start)

##2500 Insertion Sort Function
start = time.clock()
insertion_sort(sorted_Increasing2500) 
end = time.clock() 
print "2500 Increasing Insertion: " + "{:.20f}".format(end-start)
##2500 Selection Sort Function
start = time.clock()
selection_sort(sorted_Increasing2500)
end = time.clock()
print "2500 Increasing Selection: " + "{:.20f}".format(end-start)

##5000 Selection Sort Function
start = time.clock()
insertion_sort(sorted_Increasing5000)
end = time.clock()
print "5000 Increasing Insertion: " + "{:.20f}".format(end-start)
##5000 Selection Sort Fucntion 
start = time.clock()
selection_sort(sorted_Increasing5000)
end = time.clock()
print "5000 Increasing Selection: " + "{:20f}".format(end-start)

##7500 Selection Sort Function
start = time.clock()
insertion_sort(sorted_Increasing7500)
end = time.clock()
print "7500 Increasing Insertion: " + "{:.20f}".format(end-start)
##7500 Selection Sort Fucntion
start = time.clock()
selection_sort(sorted_Increasing7500)
end = time.clock()
print "7500 Increasing Selection: " + "{:20f}".format(end-start)

##10000 Selection Sort Function
start = time.clock()
insertion_sort(sorted_Increasing10000)
end = time.clock()
print "10000 Increasing Insertion: " + "{:.20f}".format(end-start)
##10000 Selection Sort Fucntion 
start = time.clock()
selection_sort(sorted_Increasing10000)
end = time.clock()
print "10000 Increasing Selection: " + "{:20f}".format(end-start)
print "##################################################################"

#Timing the Sorted Decreasing List with the two functions:
##1000 Insertion Sort Fucntion 
start = time.clock()
insertion_sort(sorted_Decreasing1000)
end = time.clock()
print "1000 Decreasing Insertion: " + "{:.20f}".format(end-start)
##1000 Selection Sort Fucntion 
start = time.clock()
selection_sort(sorted_Decreasing1000)
end = time.clock()
print "1000 Decreasing Selection: " + "{:.20f}".format(end-start)

##2500 Insertion Sort Fucntion
start = time.clock()
insertion_sort(sorted_Decreasing2500)
end = time.clock()
print "2500 Decreasing Insertion: " + "{:.20f}".format(end-start)
##2500 Selection Sort Fucntion 
start = time.clock()
selection_sort(sorted_Decreasing2500)
end = time.clock()
print "2500 Decreasing Selection: " + "{:.20f}".format(end-start)

##5000 Insertion Sort Fucntion
start = time.clock()
insertion_sort(sorted_Decreasing5000)
end = time.clock()
print "5000 Decreasing Insertion: " + "{:.20f}".format(end-start)
##5000 Selection Sort Fucntion
start = time.clock()
selection_sort(sorted_Decreasing5000)
end = time.clock()
print "5000 Decreasing Selection: " + "{:.20f}".format(end-start)

##7500 Insertion Sort Fucntion
start = time.clock()
insertion_sort(sorted_Decreasing7500)
end = time.clock()
print "7500 Decreasing Insertion: " + "{:.20f}".format(end-start)
##7500 Selection Sort Fucntion
start = time.clock()
selection_sort(sorted_Decreasing7500)
end = time.clock()
print "7500 Decreasing Selection: " + "{:.20f}".format(end-start)

##10000 Insertion Sort Fucntion
start = time.clock()
insertion_sort(sorted_Decreasing10000)
end = time.clock()
print "10000 Decreasing Insertion: " + "{:.20f}".format(end-start)
##10000 Selection Sort Fucntion
start = time.clock()
selection_sort(sorted_Decreasing10000)
end = time.clock()
print "10000 Decreasing Selection: " + "{:.20f}".format(end-start)
print "##################################################################"

#Timing the Random List with the two functions:
##1000 Insertion Sort Fucntion
start = time.clock()
insertion_sort(random_ValuesList1000)
end = time.clock()
print "1000 Random Insertion: " + "{:.20f}".format(end-start)
##1000 Selection Sort Fucntion
start = time.clock()
selection_sort(random_ValuesList2_1000)
end = time.clock()
print "1000 Random Selection: " + "{:.20f}".format(end-start)

##2500 Insertion Sort Fucntion
start = time.clock()
insertion_sort(random_ValuesList2500)
end = time.clock()
print "2500 Random Insertion: " + "{:.20f}".format(end-start)
##2500 Selection Sort Fucntion
start = time.clock()
selection_sort(random_ValuesList2_2500)
end = time.clock()
print "2500 Random Selection: " + "{:.20f}".format(end-start)

##5000 Insertion Sort Fucntion
start = time.clock()
insertion_sort(random_ValuesList5000)
end = time.clock()
print "5000 Random Insertion: " + "{:.20f}".format(end-start)
##5000 Selection Sort Fucntion
start = time.clock()
selection_sort(random_ValuesList2_5000)
end = time.clock()
print "5000 Random Selection: " + "{:.20f}".format(end-start)

##7500 Insertion Sort Fucntion
start = time.clock()
insertion_sort(random_ValuesList7500)
end = time.clock()
print "7500 Random Insertion: " + "{:.20f}".format(end-start)
##7500 Selection Sort Fucntion
start = time.clock()
selection_sort(random_ValuesList2_7500)
end = time.clock()
print "7500 Random Selection: " + "{:.20f}".format(end-start)

##10000 Insertion Sort Fucntion
start = time.clock()
insertion_sort(random_ValuesList10000)
end = time.clock()
print "10000 Random Insertion: " + "{:.20f}".format(end-start)
##10000 Selection Sort Fucntion
start = time.clock()
selection_sort(random_ValuesList2_10000)
end = time.clock()
print "10000 Random Selection: " + "{:.20f}".format(end-start)
print "##################################################################"
