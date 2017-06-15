#################################################################
# Team Name: TheRevenant
# AVL Tree Class Unit Testing Class
# Project V: AVL Trees
# CSCI 241: Data Structures and Algorithms
#################################################################
import unittest
from AVL_Binary_Search_Tree import Binary_Search_Tree


class BST_Test(unittest.TestCase):
    """Unit Testing Class for the AVL_Binary_Search_Tree Class"""

    def setUp(self):
        self._bst = Binary_Search_Tree()

    # Testing Insert Element
    def test_empty_tree(self):
        # Testing to see what an empty tree returns
        self.assertEqual('[ ]', str(self._bst), 'Empty list should print as "[ ]"')
        self.assertEqual(0, self._bst.get_height())

    def test_add_empty(self):
        # Adding a value to an empty tree
        self._bst.insert_element(12)
        self.assertEqual('[ 12 ]', str(self._bst))

    def test_add_empty_in_order(self):
        # Adding a value to an empty tree and testing In-Order
        self._bst.insert_element(12)
        self.assertEqual('[ 12 ]', str(self._bst.in_order()))

    def test_add_empty_pre_order(self):
        # Adding a value to an empty tree and testing Pre-Order
        self._bst.insert_element(12)
        self.assertEqual('[ 12 ]', str(self._bst.pre_order()))

    def test_add_empty_post_order(self):
        # Adding a value to an empty tree and testing Post-Order
        self._bst.insert_element(12)
        self.assertEqual('[ 12 ]', str(self._bst.post_order()))

    def test_add_two_empty(self):
        # Adding 2 values to an empty tree
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self.assertEqual('[ 7, 12 ]', str(self._bst))

    def test_add_two_empty_in_order(self):
        # Adding 2 values to an empty tree and testing In-Order
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self.assertEqual('[ 7, 12 ]', str(self._bst.in_order()))

    def test_add_two_empty_pre_order(self):
        # Adding 2 values to an empty tree and testing Pre-Order
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self.assertEqual('[ 12, 7 ]', str(self._bst.pre_order()))

    def test_add_two_empty_post_order(self):
        # Adding 2 values to an empty tree and testing Post-Order
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self.assertEqual('[ 7, 12 ]', str(self._bst.post_order()))

    def test_add_three_empty_order(self):
        # Adding 3 values to an empty tree
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.insert_element(3)
        self.assertEqual('[ 3, 7, 12 ]', str(self._bst))

    def test_add_three_empty_in_order(self):
        # Adding 3 values to an empty tree and testing In-Order
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.insert_element(3)
        self.assertEqual('[ 3, 7, 12 ]', str(self._bst.in_order()))

    def test_add_three_empty_pre_order(self):
        # Adding 3 values to an empty tree and testing Pre-Order
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.insert_element(3)
        self.assertEqual('[ 7, 3, 12 ]', str(self._bst.pre_order()))

    def test_add_three_empty_post_order(self):
        # Adding 3 values to an empty tree and testing Post-Order
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.insert_element(3)
        self.assertEqual('[ 3, 12, 7 ]', str(self._bst.post_order()))

    def test_add_four_empty_order(self):
        # Adding 4 values to an empty tree
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.insert_element(3)
        self._bst.insert_element(20)
        self.assertEqual('[ 3, 7, 12, 20 ]', str(self._bst))

    def test_add_four_empty_in_order(self):
        # Adding 4 values to an empty tree and testing In-Order
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.insert_element(3)
        self._bst.insert_element(20)
        self.assertEqual('[ 3, 7, 12, 20 ]', str(self._bst.in_order()))

    def test_add_four_empty_pre_order(self):
        # Adding 4 values to an empty tree and testing Pre-Order
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.insert_element(3)
        self._bst.insert_element(20)
        self.assertEqual('[ 7, 3, 12, 20 ]', str(self._bst.pre_order()))

    def test_add_four_empty_post_order(self):
        # Adding 4 values to an empty tree and testing Post-Order
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.insert_element(3)
        self._bst.insert_element(20)
        self.assertEqual('[ 3, 20, 12, 7 ]', str(self._bst.post_order()))

    # Testing Remove Element
    def test_remove_leaf_case_0(self):
        self._bst.insert_element(12)
        self._bst.remove_element(12)
        self.assertEqual('[ ]', str(self._bst))
        self.assertEqual(0, self._bst.get_height())

    def test_remove_two_case_0(self):
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.remove_element(12)
        self._bst.remove_element(7)
        self.assertEqual('[ ]', str(self._bst))

    def test_remove_two_case_1(self):
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.remove_element(7)
        self._bst.remove_element(12)
        self.assertEqual('[ ]', str(self._bst))
        self.assertEqual(0, self._bst.get_height())

    def test_remove_leaf_case_1(self):
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.insert_element(3)
        self._bst.insert_element(9)
        self._bst.insert_element(20)
        self._bst.insert_element(30)
        self._bst.insert_element(25)
        self._bst.insert_element(16)
        self._bst.remove_element(3)
        self.assertEqual('[ 12, 7, 9, 25, 20, 16, 30 ]', str(self._bst.pre_order()))
        self.assertEqual('[ 9, 7, 16, 20, 30, 25, 12 ]', str(self._bst.post_order()))
        self.assertEqual('[ 7, 9, 12, 16, 20, 25, 30 ]', str(self._bst.in_order()))
        self.assertEqual(4, self._bst.get_height())

    def test_remove_leaf_case_2(self):
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.insert_element(3)
        self._bst.insert_element(9)
        self._bst.insert_element(20)
        self._bst.insert_element(16)
        self._bst.insert_element(25)
        self._bst.remove_element(16)
        self.assertEqual('[ 12, 7, 3, 9, 20, 25 ]', str(self._bst.pre_order()))
        self.assertEqual('[ 3, 9, 7, 25, 20, 12 ]', str(self._bst.post_order()))
        self.assertEqual('[ 3, 7, 9, 12, 20, 25 ]', str(self._bst.in_order()))
        self.assertEqual(3, self._bst.get_height())

    def test_remove_case_right(self):
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.insert_element(3)
        self._bst.insert_element(9)
        self._bst.insert_element(20)
        self._bst.insert_element(10)
        self._bst.insert_element(16)
        self._bst.insert_element(25)
        self._bst.remove_element(10)
        self.assertEqual('[ 9, 7, 3, 20, 12, 16, 25 ]', str(self._bst.pre_order()))
        self.assertEqual('[ 3, 7, 16, 12, 25, 20, 9 ]', str(self._bst.post_order()))
        self.assertEqual('[ 3, 7, 9, 12, 16, 20, 25 ]', str(self._bst.in_order()))
        self.assertEqual(4, self._bst.get_height())

    def test_remove_left(self):
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.insert_element(3)
        self._bst.insert_element(9)
        self._bst.insert_element(8)
        self._bst.insert_element(20)
        self._bst.insert_element(16)
        self._bst.insert_element(25)
        self._bst.remove_element(8)
        self.assertEqual('[ 9, 7, 3, 16, 12, 20, 25 ]', str(self._bst.pre_order()))
        self.assertEqual('[ 3, 7, 12, 25, 20, 16, 9 ]', str(self._bst.post_order()))
        self.assertEqual('[ 3, 7, 9, 12, 16, 20, 25 ]', str(self._bst.in_order()))
        self.assertEqual(4, self._bst.get_height())

    def test_remove_two(self):
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.insert_element(3)
        self._bst.insert_element(9)
        self._bst.insert_element(8)
        self._bst.insert_element(20)
        self._bst.insert_element(16)
        self._bst.insert_element(25)
        self._bst.remove_element(20)
        self.assertEqual('[ 9, 7, 3, 8, 16, 12, 25 ]', str(self._bst.pre_order()))
        self.assertEqual('[ 3, 8, 7, 12, 25, 16, 9 ]', str(self._bst.post_order()))
        self.assertEqual('[ 3, 7, 8, 9, 12, 16, 25 ]', str(self._bst.in_order()))
        self.assertEqual(3, self._bst.get_height())

    def test_remove_two_children(self):
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.insert_element(3)
        self._bst.insert_element(9)
        self._bst.insert_element(8)
        self._bst.insert_element(20)
        self._bst.insert_element(16)
        self._bst.insert_element(25)
        self._bst.remove_element(7)
        self.assertEqual('[ 9, 8, 3, 16, 12, 20, 25 ]', str(self._bst.pre_order()))
        self.assertEqual('[ 3, 8, 12, 25, 20, 16, 9 ]', str(self._bst.post_order()))
        self.assertEqual('[ 3, 8, 9, 12, 16, 20, 25 ]', str(self._bst.in_order()))
        self.assertEqual(4, self._bst.get_height())

    def test_remove_root(self):
        self._bst.insert_element(12)
        self._bst.insert_element(7)
        self._bst.insert_element(3)
        self._bst.insert_element(9)
        self._bst.insert_element(8)
        self._bst.insert_element(20)
        self._bst.insert_element(16)
        self._bst.insert_element(25)
        self._bst.remove_element(9)
        self.assertEqual('[ 12, 7, 3, 8, 20, 16, 25 ]', str(self._bst.pre_order()))
        self.assertEqual('[ 3, 8, 7, 16, 25, 20, 12 ]', str(self._bst.post_order()))
        self.assertEqual('[ 3, 7, 8, 12, 16, 20, 25 ]', str(self._bst.in_order()))
        self.assertEqual(3, self._bst.get_height())


if __name__ == '__main__':
    unittest.main()


