#################################################################
# Team Name: Triceratops
# Queue Class
# Project III: Deque the Queue with Stacks of Hanoi
# CSCI 241: Data Structures and Algorithms
#################################################################
from Deque import Deque
# from file import class


class Queue:

    def __init__(self):
        self._dq = Deque()

    def __str__(self):
        return str(self._dq)

    def __len__(self):
        return len(self._dq)

    def enqueue(self, val):
        self._dq.push_front(val)

    def dequeue(self):
        if len(self._dq) == 0:
            raise IndexError
        to_return = self._dq.pop_back()
        return to_return


if __name__ == '__main__':
    # Unit tests make this unnecessary
    """
    q = Queue()
    print(q)
    q.enqueue(0)
    print(q)
    a = q.dequeue()
    print(a)
    print(q)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    q.dequeue()
    print(q)
    """
    pass
