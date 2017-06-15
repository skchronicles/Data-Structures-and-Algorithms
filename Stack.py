#################################################################
# Team Name: Triceratops
# Stack Class
# Project III: Deque the Queue with Stacks of Hanoi
# CSCI 241: Data Structures and Algorithms
#################################################################
from Deque import Deque
# from file import class

class Stack:

    def __init__(self):
        self._dq = Deque()

    def __str__(self):
        return str(self._dq)

    def __len__(self):
        return len(self._dq)

    def push(self, val):
        self._dq.push_front(val)

    def pop(self):
        if len(self._dq) == 0:
            raise IndexError
        to_return = self._dq.pop_front()
        return to_return

    def peek(self):
        if len(self._dq) == 0:
            raise IndexError
        to_return = self._dq.peek_front()
        return to_return

if __name__ == '__main__':
    # Unit tests make this unnecessary
    """
    s = Stack()
    print(s)
    s.push(0)
    print(s)
    a = len(s)
    print(a)
    b = s.pop()
    print(b)
    s.push(1)
    s.push(2)
    c = s.peek()
    print(c)
    print(s)
    """
    pass
