# editor: Liu Fen
# ID in HDU: 202320050

import unittest
from mutable import *

class TestMutableList(unittest.TestCase):

    def test_append(self):
        dict_bst = Dict_bst()
        dict_bst.insert(1, 2)
        self.assertEqual(dict_bst.Root.key, 1)
        self.assertEqual(dict_bst.Root.value, 2)
        # display(dict_bst.Root)
        dict_bst.insert(3, 4)
        lc = dict_bst.Root.right
        self.assertEqual(lc.key, 3)
        self.assertEqual(lc.value, 4)
        # display(dict_bst.Root)

    def test_delete(self):
        dict_bst = Dict_bst()
        dict_bst.insert(1, 2)
        dict_bst.insert(3, 4)
        dict_bst.insert(5, 6)
        lc = dict_bst.Root.right
        self.assertEqual(lc.key, 3)
        self.assertEqual(lc.value, 4)
        # display(dict_bst.Root)
        dict_bst.delete(3)
        lc = dict_bst.Root.right
        self.assertEqual(lc.key, 5)
        self.assertEqual(lc.value, 6)
        # display(dict_bst.Root)

    def test_size(self):
        dict_bst = Dict_bst()
        dict_bst.insert(1, 2)
        dict_bst.insert(3, 4)
        dict_bst.insert(5, 6)
        self.assertEqual(dict_bst.size(), 3)
        # print(dict_bst.size())

    def test_from_list(self):
        list = [5,6]
        dict_bst = Dict_bst()
        dict_bst.from_list(list)
        root = dict_bst.Root
        lc = root.right
        self.assertEqual(root.key, 0)
        self.assertEqual(root.value, 5)
        self.assertEqual(lc.key, 1)
        self.assertEqual(lc.value, 6)
        # display(dict_bst.Root)

    def test_to_list(self):
        dict_bst = Dict_bst()
        ls = []
        dict_bst.insert(3, 4)
        node = dict_bst.get_node(3)
        ls.append(node)
        dict_bst.insert(1, 2)
        node = dict_bst.get_node(1)
        ls.append(node)
        dict_bst.insert(5, 6)
        node = dict_bst.get_node(5)
        ls.append(node)
        list = dict_bst.to_list()
        self.assertEqual(list, ls)
        # for i in range(dict_bst.size()):
        #     print(list[i].key, list[i].value)

    def test_find(self):
        dict_bst = Dict_bst()
        dict_bst.insert(3, 4)
        dict_bst.insert(1, 2)
        dict_bst.insert(5, 6)
        node = dict_bst.get_node(5)
        node1 = dict_bst.find_key(5)
        self.assertEqual(node1, node)
        node = dict_bst.get_node1(2)
        node2 = dict_bst.find_value(2)
        self.assertEqual(node2, node)
        # print(node1.key, node1.value)
        # print(node2.key, node2.value)

    def test_filter_func(self):
        dict_bst = Dict_bst()
        dict_bst.insert(3, 4)
        dict_bst.insert(2, 5)
        # dict_bst.filter_func(dict_bst.key_is_odd)
        # self.assertEqual(dict_bst.Root.key, 2)
        # self.assertEqual(dict_bst.Root.value, 5)
        dict_bst.filter_func(dict_bst.value_is_odd)
        self.assertEqual(dict_bst.Root.key, 3)
        self.assertEqual(dict_bst.Root.value, 4)

    def test_map_func(self):
        dict_bst = Dict_bst()
        dict_bst.insert(3, 4)
        dict_bst.insert(2, 2)
        dict_bst = dict_bst.map_func(dict_bst.square)
        self.assertEqual(dict_bst.Root.key, 9)
        self.assertEqual(dict_bst.Root.value, 16)
        self.assertEqual(dict_bst.Root.left.key, 4)
        self.assertEqual(dict_bst.Root.left.value, 4)
        # display(dict_bst.Root)

    def test_reduce_func(self):
        dict_bst = Dict_bst()
        dict_bst.insert(3, 4)
        dict_bst.insert(2, 2)
        dict_bst.insert(5, 6)
        dict_bst.insert(1, 7)
        dict_bst.insert(4, 9)
        sum = dict_bst.reduce_func(dict_bst.add)
        self.assertEqual(sum.key, 15)
        self.assertEqual(sum.value, 28)
        # print(sum.key, sum.value)

    def test_iter(self):
        dict_bst = Dict_bst()
        dict_bst.insert(3, 4)
        dict_bst.insert(1, 2)
        dict_bst.insert(5, 6)
        dict_bst.insert(2, 6)
        # display(dict_bst.Root)
        dict_bst.__iter__(dict_bst.Root)
        ls = Dict_bst()
        self.assertRaises(StopIteration, lambda: ls.next())

    def test_mempty(self):
        dict_bst = Dict_bst()
        dict_bst.insert(3, 4)
        dict_bst.insert(1, 2)
        dict_bst.insert(5, 6)
        self.assertEqual(dict_bst.mempty(), None)

    def test_mconcat(self):
        dict_bst = Dict_bst()
        dict_bst.insert(3, 4)
        dict_bst.insert(1, 2)
        dict_bst.insert(5, 6)
        # display(dict_bst.Root)
        dict_bst1 = Dict_bst()
        dict_bst1.insert(6, 6)
        dict_bst = dict_bst.mconcat(dict_bst1)
        # display(dict_bst.Root)
        root = dict_bst.Root
        lc = root.left
        rc = root.right
        rrc = rc.right
        self.assertEqual(root.key, 3)
        self.assertEqual(root.value, 4)
        self.assertEqual(lc.key, 1)
        self.assertEqual(lc.value, 2)
        self.assertEqual(rc.key, 5)
        self.assertEqual(rc.value, 6)
        self.assertEqual(rrc.key, 6)
        self.assertEqual(rrc.value, 6)


def display(node):
    # print(type(node))
    if not node:
        return
    print(node.key, node.value)
    print("left")
    display(node.left)
    print("right")
    display(node.right)

if __name__ == '__main__':
    unittest.main()