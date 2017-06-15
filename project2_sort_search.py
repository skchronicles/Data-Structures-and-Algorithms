###############################################
# Skyler Kuhn
# BNFO 501: Project 2 Program
# Implementing Merge Sort
################################################
from __future__ import print_function
import time

dataFh = open("project1_data.txt", "r")
filedatalist = dataFh.read().splitlines()
dataFh.close()  # Don't forget to close your file handles

Metrics = filedatalist.pop(0)  # lets remove the zeroth element, we need this for creating two data sets
# print(Metrics)

# Grabbing the appropreiate
dataMetric, queryMetric = int(Metrics.split()[0]), int(Metrics.split()[1])
# print(dataMetric,queryMetric)  # works fine

# Checking to see if the metrics add up to the len of the new array, if not data set is crappy and the program exits
if len(filedatalist) != dataMetric + queryMetric:
    print("Error: You have crappy data. Please modify your input file. It is looks bad.")
    print(dataMetric, "+", queryMetric, "!=", len(filedatalist))
    exit()

# Creating lists for data set
datalist = filedatalist[0:dataMetric]
querylist = filedatalist[-queryMetric:]  # grab the last two things
print(datalist)
print(querylist)

# Let's get our sort on: Merge Sort
############################
# Merge Sort Method
def mergesort(list):
    if len(list) < 2:
        return list

    middle = len(list) // 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    return merge(list, left, right)

def merge(datalist, left, right):
    left.append(9999999999999999999999999999999999999999999999999999999999999999999999999999999999)  # dummy variable
    right.append(9999999999999999999999999999999999999999999999999999999999999999999999999999999999)  # dummy variable
    i, j = 0, 0
    for k in range(len(datalist)):
        if int(left[i]) <= int(right[j]):  # these are strings must convert to int's
            datalist[k] = left[i]
            i += 1
        else:
            datalist[k] = right[j]
            j += 1
    return datalist

# Let's get on to the main show: Sequential vs. Binary Search
############################
# Sequential Search Method
def sequentialSearch(dataList, query):
    """Search index-by-index to see if we have found what we are searching for."""
    for i in range(len(dataList)):
        if dataList[i] == query:
            return True
    else:  # for-else statement, if it never finds anything return False
        return False

# Now let's see if the query is in the data list!
print("Sequential Search Timing")
seqSearchOutputFH = open("project2_sequentialSearch_output.txt", "w")
seqSearchOutputFH.write("SearchTime\t\t\t\tStartTime\t\t\t\tQuery\n")  # writing a pretty header
for query in querylist:
    start = time.clock()  # starts the timer
    flag = sequentialSearch(datalist, query)
    end = time.clock()    # end the timer, we take the difference to find how long it took
    diff_ms = (end - start) * 100  # convert to ms
    if flag:  # if it is true
        #print("Yes,", query, "is in the data list!")
        print("true:{:.10f}ms\t\ttrue:0.0000000000ms\t\t{}".format(diff_ms, query))  # this, realistically, should be take out to as many sig figs as possible
        seqSearchOutputFH.write("true:{:.10f}ms\t\ttrue:0.0000000000ms\t\t{}\n".format(diff_ms, query))
    else:
        #print("No,", query, "is NOT in the data list!")
        print("false:{:.10f}ms\tfalse:0.0000000000ms\t{}".format(diff_ms, query))# this, realistically, should be take out to as many sig figs as possible
        seqSearchOutputFH.write("false:{:.10f}ms\tfalse:0.0000000000ms\t{}\n".format(diff_ms, query))

seqSearchOutputFH.close()
############################
# Binary Search Method
def binarySearch(dataList, query):
    """List needs to be pre-sorted. This function uses recursion to decrease our search window by half"""
    if len(dataList) == 0: # did not find what we are searching for, also one of the base cases.
        return False
    else:
        midindex = len(dataList) // 2  # floor division
        if dataList[midindex] == query:
            return True   #second base case, we have found what we are looking for
        else:
            if midindex < int(dataList[midindex]):  # let's look at the smaller subset of the list
                return binarySearch(dataList[:midindex], query)
            else:  # the query is larger than the midpoint, let's look at the larger subset of the list
                return binarySearch(dataList[midindex+1], query)  # +1 because we already evaulted the midpoint position


# Now let's see if the query is in the data list!
binSearchOutputFH = open("project2_binarySearch_output.txt", "w")
binSearchOutputFH.write("SearchTime\t\t\t\tStartTime\t\t\t\tQuery\n")  # writing a pretty header
print("Binary Search Timing")
datalist = mergesort(datalist)  # this needs to be sorted before we can start binary search
for query in querylist:
    start = time.clock()  # starts the timer
    flag = binarySearch(datalist, query)
    end = time.clock()  # end the timer, we take the difference to find how long it took
    diff_ms = (end - start) * 100  # convert to ms
    if flag:  # if it is true
        # print("Yes,", query, "is in the data list!")
        print("true:{:.10f}ms\t\ttrue:0.0000000000ms\t\t{}".format(diff_ms, query))
        binSearchOutputFH.write("true:{:.10f}ms\t\ttrue:0.0000000000ms\t\t{}\n".format(diff_ms, query))
    else:
        # print("No,", query, "is NOT in the data list!")
        print("false:{:.10f}ms\tfalse:0.0000000000ms\t{}".format(diff_ms, query))  # this, realistically, should be take out to as many sig figs as possible
        binSearchOutputFH.write("false:{:.10f}ms\tfalse:0.0000000000ms\t{}\n".format(diff_ms, query))

binSearchOutputFH.close()

#######################################################################################