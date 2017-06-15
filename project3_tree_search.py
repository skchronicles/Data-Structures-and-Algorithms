###############################################
# Skyler Kuhn
# BNFO 501: Project 3 Program
# Implementing a Binary Search Tree class
################################################
from __future__ import print_function
import time

class Binary_Search_Tree:
    """Base Class representing a Binary Search Tree Structure"""
    # Jet fuel can't melt binary trees #

    class _BST_Node:
        """Private class for storing linked nodes with values and references to their siblings"""
        def __init__(self, value):
            """Node Constructor with 3 attributes"""
            self._value = value     # value being added
            self._left = None       # left sibling node (if val less than parent)
            self._right = None      # right sibling node (if val greater than parent)

    def __init__(self):
        """Binary Tree Constructor (creates an empty binary tree)"""
        self._root = None     # Binary tree root

    def get_root(self):
        return self._root

    def insert_element(self, value):
        """Method to insert an element into the BST"""
        self._root = self._insert_element(value, self._root)  # insert an element, calls recursive function

    def _insert_element(self, value, node):
        """Private method to Insert elements recursively"""
        # if node._value == value:  # if we come across a value already in the list
        #    raise ValueError
        if node is None:
            return Binary_Search_Tree._BST_Node(value)
        if value < node._value:
            node._left = self._insert_element(value, node._left)
        elif value > node._value:  # if a right node child node exists
            node._right = self._insert_element(value, node._right)
        return node

    def find(self, value):
        """Return the if value is in tree"""
        current_node = self._root
        while current_node is not None:
            if value == current_node._value:
                return True
            elif value < current_node._value:
                current_node = current_node._left
            else:
                current_node = current_node._right
        return False

    def find_parent(self, value):
        """Non-recursive parent finder, uses a while loop"""
        current_node = self._root
        while current_node._value is not None:
            if current_node._left._value == value or current_node._right._value == value:
                break
            elif value < current_node._value:
                current_node = current_node._left
            else:
                current_node = current_node._right
        return current_node  # test with ._value

    def parent_finder(self, value):
        """Method to find parent, calls recursive method: _parent_finder"""
        if self._root is not None:
            return self._parent_finder(value, self._root)
        else:
            raise ValueError('The Binary Tree is Empty')

    def _parent_finder(self, value, node):
        """Private Recursive Method find calls"""
        if node._left._value == value or node._right._value == value:
            return node  # test with ._value
        elif value < node._value and node._left is not None:
            return self._parent_finder(value, node._left)
        else:
            return self._parent_finder(value, node._right)

    def remove_element(self, value):
        """Method to remove elements from Binary Tree, calls recursive method: _remove_element"""
        self._root = self._remove_element(value, self._root)

    def _remove_element(self, value, node):
        """Private, recursive method that removes a specified value from the binary tree.
        This method calls get_min and _remove_min when the node to be removed has two children"""
        if node is None:
            return node
        if value < node._value:
            node._left = self._remove_element(value, node._left)
        elif value > node._value:
            node._right = self._remove_element(value, node._right)
        elif node._left is not None and node._right is not None:  # 2 kids
            temp = self.get_min(node._right)
            node._value = temp._value
            node._right = self._remove_element(temp._value, node._right)
        elif node._left is None:  # One right child
            node = node._right
            # del temp
        else:  # One left child
            node = node._left
        return node

    def get_min(self, node):
        while node._left is not None:
            node = node._left
        return node

    def in_order(self):
        """Returns Binary Search Tree as a String in in-order, call recursive _in_order method"""
        if self._root is None:
            return '[ ]'
        else:
            return "[ " + self._in_order(self._root)[:-2] + " ]"

    def _in_order(self, node):
        return_string = ""
        if node is not None:
            return_string = self._in_order(node._left)
            return_string = return_string + str(node._value) + ", "
            return_string = return_string + self._in_order(node._right)
        return return_string

    def pre_order(self):
        """Returns Binary Search Tree as a String in pre-order, call recursive _pre_order method"""
        if self._root is None:
            return '[ ]'
        else:
            return "[ " + self._pre_order(self._root)[:-2] + " ]"

    def _pre_order(self, node):
        return_string = ""
        if node is not None:
            return_string = str(node._value) + ", "
            return_string = return_string + self._pre_order(node._left)
            return_string = return_string + self._pre_order(node._right)
        return return_string

    def post_order(self):
        """Returns Binary Search Tree as a String in post-order, call recursive _post_order method"""
        if self._root is None:
            return '[ ]'
        else:
            return "[ " + self._post_order(self._root)[:-2] + " ]"

    def _post_order(self, node):
        return_string = ""
        if node is not None:
            return_string = self._post_order(node._left)
            return_string = return_string + self._post_order(node._right)
            return_string = return_string + str(node._value) + ", "
        return return_string

    def get_height(self):
        return self._get_height(self._root)

    def _get_height(self, node):
        if node is None:
            return 0
        else:
            left_depth = self._get_height(node._left)
            right_depth = self._get_height(node._right)
            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1

    def __str__(self):
        return self.in_order()


def main():
    dataFh = open("random_testfile.txt", "r")
    #dataFh = open("project1_data.txt", "r")
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
    querylist = filedatalist[-queryMetric:]  # let's put all the queries into a list

    datalist = [int(i) for i in datalist]  # converts all the data to type int
    querylist = [int(i) for i in querylist]  # converts all the data to type int
    print(datalist)
    print(querylist)

    bst = Binary_Search_Tree()  # creating a bst object
    for input_data in datalist:
        bst.insert_element(input_data)
    print(bst)  # by default prints in-order (left, parent, right)

    # Now let's see if the query is in the data list!
    binSearchOutputFH = open("project3_binarySearchTREE_output.txt", "w")
    binSearchOutputFH.write("SearchTime\t\t\t\tStartTime\t\t\t\tQuery\n")  # writing a pretty header
    print("Binary Search Timing")

    for query in querylist:
        start = time.clock()  # starts the timer
        flag = bst.find(query)
        end = time.clock()  # end the timer, we take the difference to find how long it took
        diff_ms = (end - start) * 100  # convert to ms
        if flag:  # if it is true
            # print("Yes,", query, "is in the data list!")
            print("true:{:.10f}ms\t\ttrue:0.0000000000ms\t\t{}".format(diff_ms, query))
            binSearchOutputFH.write("true:{:.10f}ms\t\ttrue:0.0000000000ms\t\t{}\n".format(diff_ms, query))
        else:
            # print("No,", query, "is NOT in the data list!")
            print("false:{:.10f}ms\tfalse:0.0000000000ms\t{}".format(diff_ms,query))  # this, realistically, should be take out to as many sig figs as possible
            binSearchOutputFH.write("false:{:.10f}ms\tfalse:0.0000000000ms\t{}\n".format(diff_ms, query))

    binSearchOutputFH.close()



if __name__ == '__main__':
    # See Unit Test: BST_Test.py
    # pass
    main()

