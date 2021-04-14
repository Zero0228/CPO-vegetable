# editor: Liu Fen
# ID in HDU: 202320050

import unittest
from hypothesis import given
import hypothesis.strategies as st
from mutable import *

class TestMutableList(unittest.TestCase):

    def test_append(self):
        dict_bst = Dict_bst()
        dict_bst.insert(1, 2)
        self.assertEqual(dict_bst.Root.key, 1)
        self.assertEqual(dict_bst.Root.value, 2)
        # display(dict_bst.Root)
        dict_bst.insert('a', 4)
        rc = dict_bst.Root.right
        self.assertEqual(rc.key, 'a')
        self.assertEqual(rc.value, 4)
        # display(dict_bst.Root)

    def test_delete(self):
        dict_bst = Dict_bst()
        dict_bst.insert("a", 2)
        dict_bst.insert("ab", 4)
        dict_bst.insert("abc", 6)
        rc = dict_bst.Root.right
        self.assertEqual(rc.key, "ab")
        self.assertEqual(rc.value, 4)
        # display(dict_bst.Root)
        dict_bst.delete("ab")
        rc = dict_bst.Root.right
        self.assertEqual(rc.key, "abc")
        self.assertEqual(rc.value, 6)
        # display(dict_bst.Root)

    def test_size(self):
        dict_bst = Dict_bst()
        dict_bst.insert(1, 2)
        dict_bst.insert("3", 4)
        dict_bst.insert(5, None)
        self.assertEqual(dict_bst.size(), 3)
        # print(dict_bst.size())

    def test_from_list(self):
        list = [Node("a",5), Node("b", 6)]
        dict_bst = Dict_bst()
        dict_bst = dict_bst.from_list(list)
        root = dict_bst.Root
        lc = root.right
        self.assertEqual(root.key, "a")
        self.assertEqual(root.value, 5)
        self.assertEqual(lc.key, "b")
        self.assertEqual(lc.value, 6)
        # display(dict_bst.Root)

    def test_to_list(self):
        dict_bst = Dict_bst()
        self.assertEqual(dict_bst.to_list(), [])
        ls = []
        dict_bst.insert("a", 4)
        node = dict_bst.get_node("a")
        ls.append(node)
        dict_bst.insert("b", 2)
        node = dict_bst.get_node("b")
        ls.append(node)
        dict_bst.insert("c", 6)
        node = dict_bst.get_node("c")
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

    def key_is_odd(self, node):
        return node.key % 2 == 1
    def value_is_odd(self, node):
        return node.value % 2 == 1
    def test_filter_func(self):
        dict_bst = Dict_bst()
        dict_bst.insert(3, 4)
        dict_bst.insert(2, 5)
        # dict_bst.filter_func(self.key_is_odd)
        # self.assertEqual(dict_bst.Root.key, 2)
        # self.assertEqual(dict_bst.Root.value, 5)
        dict_bst.filter_func(self.value_is_odd)
        self.assertEqual(dict_bst.Root.key, 3)
        self.assertEqual(dict_bst.Root.value, 4)

    def square(self, node):
        return node.key ** 2, node.value ** 2
    def test_map_func(self):
        dict_bst = Dict_bst()
        dict_bst.insert(3, 4)
        dict_bst.insert(2, 2)
        dict_bst = dict_bst.map_func(self.square)
        self.assertEqual(dict_bst.Root.key, 9)
        self.assertEqual(dict_bst.Root.value, 16)
        self.assertEqual(dict_bst.Root.left.key, 4)
        self.assertEqual(dict_bst.Root.left.value, 4)
        # display(dict_bst.Root)

    def add(self, node1, node2) :
        return Node(node1.key+node2.key, node1.value+node2.value)
    def test_reduce_func(self):
        dict_bst = Dict_bst()
        dict_bst.insert(3, 4)
        dict_bst.insert(2, 2)
        dict_bst.insert(5, 6)
        dict_bst.insert(1, 7)
        dict_bst.insert(4, 9)
        sum = dict_bst.reduce_func(self.add)
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
        dict_bst.insert(3, None)
        dict_bst.insert("a", 2)
        dict_bst.insert(5, 6)
        self.assertEqual(dict_bst.mempty().Root, None)

    def test_mconcat(self):
        dict_bst = Dict_bst()
        dict_bst.insert(3, 4)
        dict_bst.insert("1", 2)
        dict_bst.insert(5, 6)
        # display(dict_bst.Root)
        dict_bst1 = Dict_bst()
        dict_bst1.insert("abc", 6)
        dict_bst = dict_bst.mconcat(dict_bst1)
        # display(dict_bst.Root)
        root = dict_bst.Root
        rc = root.right
        lrc = rc.left
        rrc = rc.right
        self.assertEqual(root.key, 3)
        self.assertEqual(root.value, 4)
        self.assertEqual(rc.key, "1")
        self.assertEqual(rc.value, 2)
        self.assertEqual(lrc.key, 5)
        self.assertEqual(lrc.value, 6)
        self.assertEqual(rrc.key, "abc")
        self.assertEqual(rrc.value, 6)


    NodeStrategy = st.builds(Node, st.one_of(st.integers(),st.text(min_size=1)), st.one_of(st.integers(),st.text(min_size=1)))
    @given(st.lists(NodeStrategy))
    def test_from_list_to_list(self, arr):
        k = 0
        for i in arr:
            arr1 = arr.copy()[k+1:]
            for j in arr1:
                if i == j:
                    arr.remove(j)
            k = k + 1
        if len(arr)>2:
            arr = sorted(arr)
        dict_bst = Dict_bst().from_list(arr)
        tmp_bst = dict_bst.to_list()
        if len(arr)>0:
            for i in range(len(arr)):
                self.assertEqual(arr[i].key_sum==tmp_bst[i].key_sum, True)
                self.assertEqual(arr[i].value, tmp_bst[i].value)

    @given(st.lists(NodeStrategy))
    def test_len_size(self, arr):
        k = 0
        for i in arr:
            arr1 = arr.copy()[k + 1:]
            for j in arr1:
                if i == j:
                    arr.remove(j)
            k = k + 1
        dict_bst = Dict_bst()
        for i in arr:
            dict_bst.insert(i.key, i.value)
        self.assertEqual(dict_bst.size(), len(arr))

    @given(st.lists(NodeStrategy))
    def test_monoid_identity(self, arr):
        k = 0
        for i in arr:
            arr1 = arr.copy()[k + 1:]
            for j in arr1:
                if i == j:
                    arr.remove(j)
            k = k + 1
        dict_bst = Dict_bst()
        for i in arr:
            dict_bst.insert(i.key, i.value)
        dict_bst_empty = dict_bst.mempty()
        self.assertEqual(dict_bst.mconcat(dict_bst_empty), dict_bst)
        self.assertEqual(dict_bst_empty.mconcat(dict_bst), dict_bst)
        self.assertEqual(dict_bst.mconcat(dict_bst_empty), dict_bst_empty.mconcat(dict_bst))

    @given(st.lists(NodeStrategy), st.lists(NodeStrategy), st.lists(NodeStrategy))
    def test_monoid_associativity(self, arr, arr1, arr2):
        k = 0
        for i in arr:
            arr0 = arr.copy()[k + 1:]
            for j in arr0:
                if i == j:
                    arr.remove(j)
            k = k + 1
        dict_bst = Dict_bst()
        for i in arr:
            dict_bst.insert(i.key, i.value)
        k = 0
        for i in arr1:
            arr0 = arr1.copy()[k + 1:]
            for j in arr0:
                if i == j:
                    arr1.remove(j)
            k = k + 1
        dict_bst1 = Dict_bst()
        for i in arr1:
            dict_bst1.insert(i.key, i.value)
        k = 0
        for i in arr2:
            arr0 = arr2.copy()[k + 1:]
            for j in arr0:
                if i == j:
                    arr2.remove(j)
            k = k + 1
        dict_bst2 = Dict_bst()
        for i in arr2:
            dict_bst2.insert(i.key, i.value)
        self.assertEqual(dict_bst.mconcat(dict_bst1).mconcat(dict_bst2), dict_bst.mconcat(dict_bst1.mconcat(dict_bst2)))

# def display(node):
#     # print(type(node))
#     if not node:
#         return
#     print(node.key, node.value)
#     print("left")
#     display(node.left)
#     print("right")
#     display(node.right)

if __name__ == '__main__':
    unittest.main()