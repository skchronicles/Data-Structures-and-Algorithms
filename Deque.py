#################################################################
# Team Name: Triceratops
# Deque Class
# Project III: Deque the Queue with Stacks of Hanoi
# CSCI 241: Data Structures and Algorithms
#################################################################
from Linked_List import Linked_List
# from file import class

class Deque:
    """Deque Abstract Data type: Data can be access from  both the front and back end (not in the middle)"""
    def __init__(self):
        self._list = Linked_List()

    def __str__(self):
        return str(self._list)

    def __len__(self):
        return len(self._list)

    def push_front(self, val):
        """Front is the head of the Linked List"""
        if len(self._list) == 0:
            self._list.append_element(val)
        else:
            self._list.insert_element_at(val, 0)
  
    def pop_front(self):
        """Front is the head of the Linked List"""
        if len(self._list) == 0:
            raise IndexError
        to_return = self._list.remove_element_at(0)
        return to_return

    def peek_front(self):
        """Front is the head of the Linked List"""
        if len(self._list) == 0:
            raise IndexError
        to_return = self._list.get_element_at(0)
        return to_return

    def push_back(self, val):
        """Back is the tail of the linked list"""
        self._list.append_element(val)
  
    def pop_back(self):
        """Back is the tail of the linked list"""
        if len(self._list) == 0:
            raise IndexError
        to_return = self._list.remove_element_at(len(self._list) - 1)
        return to_return

    def peek_back(self):
        """Back is the tail of the linked list"""
        if len(self._list) == 0:
            raise IndexError
        to_return = self._list.get_element_at(len(self._list) - 1)
        return to_return

if __name__ == '__main__':
    # Unit tests make this unnecessary
    """
    d = Deque()
    d.push_front(12)
    d.push_back(13)
    b = d.pop_back()
    print("Value popped from the back: " + str(b))
    c = d.pop_front()
    print("Value popped from the front: " + str(c))
    d.push_back(1)
    d.push_front(0)
    d.push_front(-1)
    d.push_back(2)
    a = d.peek_front()
    print("Peek of the front: " + str(a))
    e = d.peek_back()
    print("Peek of the back: " + str(e))
    print("Values in Deque: "+ str(d))
    d.pop_front()
    d.pop_back()
    print("New Values in list after popping the front and Back: " + str(d))
    """
    pass
