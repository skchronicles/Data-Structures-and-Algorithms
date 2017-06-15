######################################################################
# Skyler Kuhn
# This is a small script to create test a random test file to input into any of the programs.
######################################################################
import random

random.seed(123)

dataSize = 100000
queriesSize = 50000

testfileFH = open("random_testfile.txt", "w")
testfileFH.write("{}\t{}\n".format(dataSize,queriesSize))

datalist = [x for x in range(dataSize)]
querylist = [x for x in range(queriesSize)]

random.shuffle(datalist)
random.shuffle(querylist)
# print(datalist)
# print(querylist)

for i in datalist:
    testfileFH.write("{}\n".format(i))

for i in querylist:
    testfileFH.write("{}\n".format(i))

