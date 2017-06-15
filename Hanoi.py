#################################################################
# Team Name: Triceratops
# Hanoi Class: Uses the Stack Class
# Project III: Deque the Queue with Stacks of Hanoi
# CSCI 241: Data Structures and Algorithms
#################################################################
import time
from Stack import Stack

def Hanoi_rec(n, s, a, d):
    print(n, s, a, d)
    if n == 0:
        d.push(s.pop())
    else:
        Hanoi_rec(n - 1, s, d, a)
        d.push(s.pop())
        Hanoi_rec(n - 1, a, s, d)
    print(n, s, a, d)
    print()

def Hanoi(n):
    source = Stack()
    dest = Stack()
    aux = Stack()
    i = n-1
    while i >= 0:
        source.push(i)
        i = i - 1
    Hanoi_rec(n-1, source, aux, dest)

if __name__ == '__main__':
    start = time.clock()
    n = 20  # changes the number of stacks
    Hanoi(n)
    end = time.clock()
    print('computed Hanoi(' + str(n) + ') in ' + str(end - start) + ' seconds.')
