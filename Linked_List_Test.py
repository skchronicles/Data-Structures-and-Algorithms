import unittest
from Linked_List import Linked_List

class Linked_Lest_Tester(unittest.TestCase):

    def setUp(self):
        self._string_list = Linked_List()

    def test_empty_list_string(self):
        self.assertEqual('[ ]', str(self._string_list), 'Empty list should print as "[ ]"')

    def test_add_head_empty(self):
        self._string_list.append_element('Victory')
        self.assertEqual('[ Victory ]', str(self._string_list))

    def test_add_tail_with_one(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        self.assertEqual('[ Data, Structures ]', str(self._string_list))

    def test_add_head_with_one(self):
        self._string_list.append_element('Structures')
        self._string_list.insert_element_at('Data', 0)
        self.assertEqual('[ Data, Structures ]', str(self._string_list))

    def test_add_head_with_two(self):
        self._string_list.append_element('Structures')
        self._string_list.append_element('Rocks')
        self._string_list.insert_element_at('Data', 0)
        self.assertEqual('[ Data, Structures, Rocks ]', str(self._string_list))

    def test_add_tail_with_two(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        self._string_list.append_element('Rocks')
        self.assertEqual('[ Data, Structures, Rocks ]', str(self._string_list))

    def test_add_middle_with_two(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Rocks')
        self._string_list.insert_element_at('Structures', 1)
        self.assertEqual('[ Data, Structures, Rocks ]', str(self._string_list))

    def test_add_second_of_four(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('and')
        self._string_list.append_element('Algorithms')
        self._string_list.insert_element_at('Structures', 1)
        self.assertEqual('[ Data, Structures, and, Algorithms ]', str(self._string_list))

    def test_add_third_of_four(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        self._string_list.append_element('Algorithms')
        self._string_list.insert_element_at('and', 2)
        self.assertEqual('[ Data, Structures, and, Algorithms ]', str(self._string_list))
  
    def test_get_empty_length(self):
        self.assertEqual(0, len(self._string_list))

    def test_get_one_length(self):
        self._string_list.append_element('Victory')
        self.assertEqual(1, len(self._string_list))

    def test_get_two_length_append(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        self.assertEqual(2, len(self._string_list))

    def test_get_two_length_insert(self):
        self._string_list.append_element('Structures')
        self._string_list.insert_element_at('Data', 0)
        self.assertEqual(2, len(self._string_list))

    def test_get_three_length_insert(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Rocks')
        self._string_list.insert_element_at('Structures', 1)
        self.assertEqual(3, len(self._string_list))

    def test_remove_head_leaving_zero_returned_value(self):
        self._string_list.append_element('Victory')
        returned = self._string_list.remove_element_at(0)
        self.assertEqual('Victory', returned)

    def test_remove_head_leaving_zero_remaining_list(self):
        self._string_list.append_element('Victory')
        returned = self._string_list.remove_element_at(0)
        self.assertEqual('[ ]', str(self._string_list))

    def test_remove_head_leaving_zero_length(self):
        self._string_list.append_element('Victory')
        returned = self._string_list.remove_element_at(0)
        self.assertEqual(0, len(self._string_list))

    def test_remove_head_leaving_one_returned_value(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        returned = self._string_list.remove_element_at(0)
        self.assertEqual('Data', returned)

    def test_remove_head_leaving_one_remaining_list(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        returned = self._string_list.remove_element_at(0)
        self.assertEqual('[ Structures ]', str(self._string_list))

    def test_removeHeadLeavingOneLength(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        returned = self._string_list.remove_element_at(0)
        self.assertEqual(1, len(self._string_list))

    def test_remove_tail_leaving_one_returned_value(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        returned = self._string_list.remove_element_at(1)
        self.assertEqual('Structures', returned)

    def test_remove_tail_leaving_one_remaining_list(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        returned = self._string_list.remove_element_at(1)
        self.assertEqual('[ Data ]', str(self._string_list))

    def test_remove_tail_leaving_one_length(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        returned = self._string_list.remove_element_at(1)
        self.assertEqual(1, len(self._string_list))

    def test_remove_middle_leaving_two_returned_value(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        self._string_list.append_element('Rocks')
        returned = self._string_list.remove_element_at(1)
        self.assertEqual('Structures', returned)

    def test_remove_middle_leaving_two_remaining_list(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        self._string_list.append_element('Rocks')
        returned = self._string_list.remove_element_at(1)
        self.assertEqual('[ Data, Rocks ]', str(self._string_list))

    def test_remove_middle_leaving_two_length(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        self._string_list.append_element('Rocks')
        returned = self._string_list.remove_element_at(1)
        self.assertEqual(2, len(self._string_list))
  
    def test_get_head_with_one_element(self):
        self._string_list.append_element('Victory')
        returned = self._string_list.get_element_at(0)
        self.assertEqual('Victory', returned)

    def test_get_head_with_one_element_remaining(self):
        self._string_list.append_element('Victory')
        returned = self._string_list.get_element_at(0)
        self.assertEqual('[ Victory ]', str(self._string_list))

    def test_get_head_with_one_element_length(self):
        self._string_list.append_element('Victory')
        returned = self._string_list.get_element_at(0)
        self.assertEqual(1, len(self._string_list))

    def test_get_tail_with_two_elements(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        returned = self._string_list.get_element_at(1)
        self.assertEqual('Structures', returned)

    def test_get_tail_with_two_elements_remaining(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        returned = self._string_list.get_element_at(1)
        self.assertEqual('[ Data, Structures ]', str(self._string_list))

    def test_get_tail_with_two_elements_length(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        returned = self._string_list.get_element_at(1)
        self.assertEqual(2, len(self._string_list))

    def test_get_middle_with_three_elements(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        self._string_list.append_element('Rocks')
        returned = self._string_list.get_element_at(1)
        self.assertEqual('Structures', returned)

    def test_get_middle_with_three_elements_remaining(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        self._string_list.append_element('Rocks')
        returned = self._string_list.get_element_at(1)
        self.assertEqual('[ Data, Structures, Rocks ]', str(self._string_list))

    def test_get_middle_with_three_elements_length(self):
        self._string_list.append_element('Data')
        self._string_list.append_element('Structures')
        self._string_list.append_element('Rocks')
        returned = self._string_list.get_element_at(1)
        self.assertEqual(3, len(self._string_list))

    def test_add_at_negative_index_ignore(self):
        with self.assertRaises(IndexError):
            self._string_list.insert_element_at('Victory', -1)
        self.assertEqual('[ ]', str(self._string_list))

    def test_remove_at_negative_index_ignore(self):
        with self.assertRaises(IndexError):
            returned = self._string_list.remove_element_at(-1)
        self.assertEqual('[ ]', str(self._string_list))

    def test_get_at_negative_index_ignore(self):
        with self.assertRaises(IndexError):
            returned = self._string_list.get_element_at(-1)
        self.assertEqual('[ ]', str(self._string_list))

    def test_add_at_zero_index_empty_ignore(self):
        with self.assertRaises(IndexError):
            self._string_list.insert_element_at('Victory', 0)
        self.assertEqual('[ ]', str(self._string_list))

    def test_remove_at_zero_index_empty_ignore(self):
        with self.assertRaises(IndexError):
            returned = self._string_list.remove_element_at(0)
        self.assertEqual('[ ]', str(self._string_list))

    def test_get_at_zero_index_empty_ignore(self):
        with self.assertRaises(IndexError):
            returned = self._string_list.get_element_at(0)
        self.assertEqual('[ ]', str(self._string_list))

    def test_add_at_one_past_index_ignore(self):
        self._string_list.append_element('Data')
        with self.assertRaises(IndexError):
            self._string_list.insert_element_at('Structures', 1)
        self.assertEqual('[ Data ]', str(self._string_list))

    def test_remove_at_one_past_index_ignore(self):
        self._string_list.append_element('Data')
        with self.assertRaises(IndexError):
            returned = self._string_list.remove_element_at(1)
        self.assertEqual('[ Data ]', str(self._string_list))

    def test_get_at_one_past_index_ignore(self):
        self._string_list.append_element('Data')
        with self.assertRaises(IndexError):
            returned = self._string_list.get_element_at(1)
        self.assertEqual('[ Data ]', str(self._string_list))

    def test_empty_iterator(self):
        for value in self._string_list:
            self.fail()

    def test_one_iterator(self):
        self._string_list.append_element('Data')
        count = 0
        for value in self._string_list:
            self.assertEqual('Data', value)
            count = count + 1
        self.assertEqual(1, count)

    def test_multiple_iterator(self):
        strs = ['Data', 'Structures', 'Rocks']
        self._string_list.append_element(strs[0])
        self._string_list.append_element(strs[1])
        self._string_list.append_element(strs[2])
        count = 0
        for value in self._string_list:
            self.assertEqual(strs[count], value)
            count = count + 1
        self.assertEqual(3, count)

  
if __name__ == '__main__':
    unittest.main()
