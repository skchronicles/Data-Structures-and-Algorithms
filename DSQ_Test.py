#################################################################
# Team Name: Triceratops
# Deque, Stacks, and Queue Unit Testing Class
# Project III: Deque the Queue with Stacks of Hanoi
# CSCI 241: Data Structures and Algorithms
#################################################################
import unittest
from Deque import Deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):

    def setUp(self):
        self._deque = Deque()
        self._stack = Stack()
        self._queue = Queue()

    def test_empty_list_string(self):
        self.assertEqual('[ ]', str(self._deque), 'Empty list should print as "[ ]"')
        self.assertEqual('[ ]', str(self._stack), 'Empty list should print as "[ ]"')
        self.assertEqual('[ ]', str(self._queue), 'Empty list should print as "[ ]"')

    def test_add_empty(self):
        # Checking Deque
        self._deque.push_front('Victory')
        self.assertEqual('[ Victory ]', str(self._deque))
        self. _deque.pop_back()
        self._deque.push_back('Victory')
        self.assertEqual('[ Victory ]', str(self._deque))
        # Checking Stack
        self._stack.push('Victory')
        self.assertEqual('[ Victory ]', str(self._stack))
        # Checking Queue
        self._queue.enqueue('Victory')
        self.assertEqual('[ Victory ]', str(self._queue))

    def test_add_with_one(self):
        # Checking Deque
        self._deque.push_front('Data')
        self._deque.push_back('Structures')
        self.assertEqual('[ Data, Structures ]', str(self._deque))
        # Checking Stack
        self._stack.push('Victory')
        self._stack.push('Structures')
        self.assertEqual('[ Structures, Victory ]', str(self._stack))
        # Checking Queue
        self._queue.enqueue('Victory')
        self._queue.enqueue('Structures')
        self.assertEqual('[ Structures, Victory ]', str(self._queue))

    def test_add_with_two(self):
        # Checking Deque
        self._deque.push_front('Data')
        self._deque.push_back('Structures')
        self._deque.push_back('Rocks!')
        self.assertEqual('[ Data, Structures, Rocks! ]', str(self._deque))
        # Checking Stack
        self._stack.push('Victory')
        self._stack.push('Structures')
        self._stack.push('Rocks')
        self.assertEqual('[ Rocks, Structures, Victory ]', str(self._stack))
        # Checking Queue
        self._queue.enqueue('Victory')
        self._queue.enqueue('Structures')
        self._queue.enqueue('Rocks')
        self.assertEqual('[ Rocks, Structures, Victory ]', str(self._queue))

    def test_remove_with_three(self):
        self._deque.push_front('Data')
        self._deque.push_back('Structures')
        self._deque.push_back('Rocks!')
        self._deque.pop_front()  # removes the front in the front or head position
        self.assertEqual('[ Structures, Rocks! ]', str(self._deque))
        # Checking Stack
        self._stack.push('Victory')
        self._stack.push('Structures')
        self._stack.push('Rocks')
        self._stack.pop()  # removes the last value put in
        self.assertEqual('[ Structures, Victory ]', str(self._stack))
        # Checking Queue
        self._queue.enqueue('Victory')
        self._queue.enqueue('Structures')
        self._queue.enqueue('Rocks')
        self._queue.dequeue()  # the first value put in
        self.assertEqual('[ Rocks, Structures ]', str(self._queue))

    def test_remove_two_with_three(self):
        self._deque.push_front('Data')
        self._deque.push_back('Structures')
        self._deque.push_back('Rocks!')
        self._deque.pop_front()  # removes the front in the front or head position
        self._deque.pop_back()   # removes the front in the back or tail position
        self.assertEqual('[ Structures ]', str(self._deque))
        # Checking Stack
        self._stack.push('Victory')
        self._stack.push('Structures')
        self._stack.push('Rocks')
        self._stack.pop()  # removes the last value put in
        self._stack.pop()  # removes the last value put in
        self.assertEqual('[ Victory ]', str(self._stack))
        # Checking Queue
        self._queue.enqueue('Victory')
        self._queue.enqueue('Structures')
        self._queue.enqueue('Rocks')
        self._queue.dequeue()  # the first value put in
        self._queue.dequeue()  # the first value put in
        self.assertEqual('[ Rocks ]', str(self._queue))

    def test_remove_three_with_three(self):
        self._deque.push_front('Data')
        self._deque.push_back('Structures')
        self._deque.push_back('Rocks!')
        self._deque.pop_front()  # removes the front in the front or head position
        self._deque.pop_back()   # removes the front in the back or tail position
        self._deque.pop_back()   # removes the front in the back or tail position
        self.assertEqual('[ ]', str(self._deque))
        # Checking Stack
        self._stack.push('Victory')
        self._stack.push('Structures')
        self._stack.push('Rocks')
        self._stack.pop()  # removes the last value put in
        self._stack.pop()  # removes the last value put in
        self._stack.pop()  # removes the last value put in
        self.assertEqual('[ ]', str(self._stack))
        # Checking Queue
        self._queue.enqueue('Victory')
        self._queue.enqueue('Structures')
        self._queue.enqueue('Rocks')
        self._queue.dequeue()  # the first value put in
        self._queue.dequeue()  # the first value put in
        self._queue.dequeue()  # the first value put in
        self.assertEqual('[ ]', str(self._queue))

    def test_return_removed(self):
        self._deque.push_front('Data')
        returning = self._deque.pop_front()  # removes the front in the front or head position
        self._deque.push_front('Structures')
        to_return = self._deque.pop_back()
        self.assertEqual('Data', str(returning))
        self.assertEqual('Structures', str(to_return))
        # Checking Stack
        self._stack.push('Victory')
        returning = self._stack.pop()  # removes the last value put in
        self.assertEqual('Victory', str(returning))
        # Checking Queue
        self._queue.enqueue('Victory')
        returning = self._queue.dequeue()  # the first value put in
        self.assertEqual('Victory', str(returning))

    def test_return_with_three(self):
        self._deque.push_front('Data')
        self._deque.push_back('Structures')
        self._deque.push_back('Rocks!')
        returning = self._deque.pop_front()  # removes the front in the front or head position
        to_return = self._deque.pop_back()  # removes the front in the back or tail position
        self.assertEqual('Data', str(returning))
        self.assertEqual('Rocks!', str(to_return))
        # Checking Stack
        self._stack.push('Victory')
        self._stack.push('Structures')
        self._stack.push('Rocks')
        returning = self._stack.pop()  # removes the last value put in
        to_return = self._stack.pop()  # removes the last value put in
        self.assertEqual('Rocks', str(returning))
        self.assertEqual('Structures', str(to_return))
        # Checking Queue
        self._queue.enqueue('Victory')
        self._queue.enqueue('Structures')
        self._queue.enqueue('Rocks')
        returning = self._queue.dequeue()  # the first value put in
        to_return = self._queue.dequeue()  # the first value put in
        self.assertEqual('Victory', str(returning))
        self.assertEqual('Structures', str(to_return))

    def test_get_empty_length(self):
        # Checking Deque
        self.assertEqual(0, len(self._deque))
        # Checking Stack
        self.assertEqual(0, len(self._stack))
        # Checking Queue
        self.assertEqual(0, len(self._queue))

    def test_get_add_one_length(self):
        # Checking Deque
        self._deque.push_front('Data')
        self.assertEqual(1, len(self._deque))
        # Checking Stack
        self._stack.push('Victory')
        self.assertEqual(1, len(self._stack))
        # Checking Queue
        self._queue.enqueue('Victory')
        self.assertEqual(1, len(self._queue))

    def test_get_add_two_length(self):
        # Checking Deque
        self._deque.push_front('Data')
        self._deque.push_front('Data2')
        self.assertEqual(2, len(self._deque))
        # Checking Stack
        self._stack.push('Victory')
        self._stack.push('Victory2')
        self.assertEqual(2, len(self._stack))
        # Checking Queue
        self._queue.enqueue('Victory')
        self._queue.enqueue('Victory2')
        self.assertEqual(2, len(self._queue))

    def test_get_add_two_minus_one_length(self):
        # Checking Deque
        self._deque.push_front('Data')
        self._deque.push_front('Data2')
        self._deque.pop_back()
        self.assertEqual(1, len(self._deque))
        # Checking Stack
        self._stack.push('Victory')
        self._stack.push('Victory2')
        self._stack.pop()
        self.assertEqual(1, len(self._stack))
        # Checking Queue
        self._queue.enqueue('Victory')
        self._queue.enqueue('Victory2')
        self._queue.dequeue()
        self.assertEqual(1, len(self._queue))

    def test_get_add_two_minus_two_length(self):
        # Checking Deque
        self._deque.push_front('Data')
        self._deque.push_front('Data2')
        self._deque.pop_back()
        self._deque.pop_front()
        self.assertEqual(0, len(self._deque))
        # Checking Stack
        self._stack.push('Victory')
        self._stack.push('Victory2')
        self._stack.pop()
        self._stack.pop()
        self.assertEqual(0, len(self._stack))
        # Checking Queue
        self._queue.enqueue('Victory')
        self._queue.enqueue('Victory2')
        self._queue.dequeue()
        self._queue.dequeue()
        self.assertEqual(0, len(self._queue))

    def test_remove_from_empty_index_ignore(self):
        # Checking Deque
        with self.assertRaises(IndexError):
            self._deque.pop_back()
        self.assertEqual('[ ]', str(self._deque))
        with self.assertRaises(IndexError):
            self._deque.pop_front()
        self.assertEqual('[ ]', str(self._deque))
        # Checking Stack
        with self.assertRaises(IndexError):
            self._stack.pop()
        self.assertEqual('[ ]', str(self._stack))
        # Checking Queue
        with self.assertRaises(IndexError):
            self._queue.dequeue()
        self.assertEqual('[ ]', str(self._queue))

    def test_return_peek(self):
        # Checking Deque
        self._deque.push_front('Data')
        returning = self._deque.peek_front()  # removes the front in the front or head position
        self._deque.push_front('Structures')
        to_return = self._deque.peek_back()
        self.assertEqual('Data', str(returning))
        self.assertEqual('Data', str(to_return))
        # Checking Stack
        self._stack.push('Victory')
        returning = self._stack.peek()  # removes the last value put in
        self.assertEqual('Victory', str(returning))

    def test_return_peek_with_three(self):
        self._deque.push_front('Data')
        self._deque.push_back('Structures')
        self._deque.push_back('Rocks!')
        returning = self._deque.peek_front()  # removes the front in the front or head position
        to_return = self._deque.peek_back()  # removes the front in the back or tail position
        self.assertEqual('Data', str(returning))
        self.assertEqual('Rocks!', str(to_return))
        # Checking Stack
        self._stack.push('Victory')
        self._stack.push('Structures')
        self._stack.push('Rocks')
        returning = self._stack.peek()  # removes the last value put in
        self.assertEqual('Rocks', str(returning))

if __name__ == '__main__':
  unittest.main()
