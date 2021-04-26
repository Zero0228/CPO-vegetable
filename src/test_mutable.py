# editor: Liu Fen
# ID in HDU: 202320050

import unittest
from hypothesis import given
import hypothesis.strategies as st
from mutable import *

class TestMutableList(unittest.TestCase):

    def test_insert(self):
        dict_bst = Dict_bst()
        dict_bst.insert(1, 2)
        self.assertEqual(dict_bst.Root.key, 1)
        self.assertEqual(dict_bst.Root.value, 2)
        self.assertEqual(Dict_bst((1,2),('a',4)).Root.right.key, 'a')
        self.assertEqual(Dict_bst((1,2),('a',4)).Root.right.value, 4)
        try:  Dict_bst((None,1))
        except TypeError as e:
            self.assertEqual(e.args[0], "The key value cannot be None")

    def test_delete(self):
        self.assertEqual(Dict_bst(("a", 2),("ab", 4),("abc", 6)).Root.right.key, "ab")
        self.assertEqual(Dict_bst(("a", 2),("ab", 4),("abc", 6)).Root.right.value, 4)
        dict_bst = Dict_bst(("a", 2),("ab", 4),("abc", 6))
        dict_bst.delete("ab")
        self.assertEqual(dict_bst.Root.right.key, "abc")
        self.assertEqual(dict_bst.Root.right.value, 6)
        try:  dict_bst.delete(1)
        except AttributeError as e:
            self.assertEqual(e.args[0], "The element does not exist")

    def test_size(self):
        self.assertEqual(Dict_bst((1, 2),("3", 4),(5, None)).size(), 3)
        self.assertEqual(Dict_bst().size(), 0)

    def test_from_list(self):
        list = [Node("a",5), Node("b", 6)]
        dict_bst = Dict_bst().from_list(list)
        self.assertEqual(dict_bst.Root.key, "a")
        self.assertEqual(dict_bst.Root.value, 5)
        self.assertEqual(dict_bst.Root.right.key, "b")
        self.assertEqual(dict_bst.Root.right.value, 6)
        list1 = []
        dict_bst = Dict_bst()
        self.assertEqual(dict_bst.from_list(list1), dict_bst)

    def test_to_list(self):
        self.assertEqual(Dict_bst().to_list(), [])
        dict_bst = Dict_bst(("a", 4), ("b", 2), ("c", 6))
        ls = [dict_bst.get_node("a"),dict_bst.get_node("b"),dict_bst.get_node("c")]
        self.assertEqual(dict_bst.to_list(), ls)

    def test_find(self):
        dict_bst = Dict_bst((3, 4),(1, 2),(5, 6))
        self.assertEqual(dict_bst.find_key(5), dict_bst.get_node(5))
        self.assertEqual(dict_bst.find_value(2), dict_bst.get_node1(2))

    def key_is_odd(self, node):
        return node.key % 2 == 1
    def value_is_odd(self, node):
        return node.value % 2 == 1
    def test_filter_func_value(self):
        dict_bst = Dict_bst((3, 4),(2, 5))
        dict_bst.filter_func(self.value_is_odd)
        self.assertEqual(dict_bst.Root.key, 3)
        self.assertEqual(dict_bst.Root.value, 4)
    def test_filter_func_key(self):
        dict_bst = Dict_bst((3, 4),(2, 5))
        dict_bst.filter_func(self.key_is_odd)
        self.assertEqual(dict_bst.Root.key, 2)
        self.assertEqual(dict_bst.Root.value, 5)

    def square(self, node):
        return node.key ** 2, node.value ** 2
    def test_map_func(self):
        dict_bst = Dict_bst((3, 4),(2, 2))
        dict_bst = dict_bst.map_func(self.square)
        self.assertEqual(dict_bst.Root.key, 9)
        self.assertEqual(dict_bst.Root.value, 16)
        self.assertEqual(dict_bst.Root.left.key, 4)
        self.assertEqual(dict_bst.Root.left.value, 4)

    def add(self, node1, node2) :
        return Node(node1.key+node2.key, node1.value+node2.value)
    def test_reduce_func(self):
        sum = Dict_bst((3, 4),(2, 2),(5, 6),(1, 7),(4, 9)).reduce_func(self.add)
        self.assertEqual(sum.key, 15)
        self.assertEqual(sum.value, 28)

    def test_iter(self):
        list = [Node(3,4), Node(1,2), Node("1",2)]
        dict_bst = Dict_bst().from_list(list)
        tmp = []
        for e in dict_bst:
            tmp.append(e)
        self.assertEqual(list, tmp)
        # test that the two iterators on one data structure should work in parallel correctly
        i1 = dict_bst.__iter__()
        i2 = dict_bst.__iter__()
        self.assertEqual(next(i1), dict_bst.find_key(3))
        self.assertEqual(next(i1), dict_bst.find_key(1))
        self.assertEqual(next(i2), dict_bst.find_key(3))
        self.assertEqual(next(i2), dict_bst.find_key(1))
        self.assertEqual(next(i1), dict_bst.find_key("1"))

        self.assertEqual(dict_bst.to_list(), tmp)
        dict_bst.__iter__()
        ls = Dict_bst()
        self.assertRaises(StopIteration, lambda: ls.next())

    def test_mempty(self):
        self.assertEqual(Dict_bst((3, None),("a", 2),(5, 6)).mempty().Root, None)

    def test_mconcat(self):
        dict_bst = Dict_bst((3, 4),("1", 2),(5, 6)).mconcat(Dict_bst(("abc", 6)))
        self.assertEqual(dict_bst.Root.key, 3)
        self.assertEqual(dict_bst.Root.value, 4)
        self.assertEqual(dict_bst.Root.right.key, "1")
        self.assertEqual(dict_bst.Root.right.value, 2)
        self.assertEqual(dict_bst.Root.right.left.key, 5)
        self.assertEqual(dict_bst.Root.right.left.value, 6)
        self.assertEqual(dict_bst.Root.right.right.key, "abc")
        self.assertEqual(dict_bst.Root.right.right.value, 6)

    def de_duplication(self, arr):
        k = 0
        for i in arr:
            arr1 = arr.copy()[k + 1:]
            for j in arr1:
                if i == j:  arr.remove(j)
            k = k + 1
        return arr

    NodeStrategy = st.builds(Node, st.one_of(st.integers(),st.text(min_size=1)), st.one_of(st.integers(),st.text(min_size=1)))
    @given(st.lists(NodeStrategy))
    def test_from_list_to_list(self, arr):
        arr = self.de_duplication(arr)
        if len(arr)>2:  arr = sorted(arr)
        dict_bst = Dict_bst().from_list(arr)
        tmp_bst = dict_bst.to_list()
        if len(arr)>0:
            for i in range(len(arr)):
                self.assertEqual(arr[i].key_sum==tmp_bst[i].key_sum, True)
                self.assertEqual(arr[i].value, tmp_bst[i].value)

    @given(st.lists(NodeStrategy))
    def test_len_size(self, arr):
        arr = self.de_duplication(arr)
        self.assertEqual(Dict_bst().from_list(arr).size(), len(arr))

    @given(st.lists(NodeStrategy))
    def test_monoid_identity(self, arr):
        arr = self.de_duplication(arr)
        dict_bst = Dict_bst().from_list(arr)
        dict_bst_empty = dict_bst.mempty()
        self.assertEqual(dict_bst.mconcat(dict_bst_empty), dict_bst)
        self.assertEqual(dict_bst_empty.mconcat(dict_bst), dict_bst)
        self.assertEqual(dict_bst.mconcat(dict_bst_empty), dict_bst_empty.mconcat(dict_bst))

    @given(st.lists(NodeStrategy), st.lists(NodeStrategy), st.lists(NodeStrategy))
    def test_monoid_associativity(self, arr, arr1, arr2):
        arr = self.de_duplication(arr)
        dict_bst = Dict_bst().from_list(arr)
        arr1 = self.de_duplication(arr1)
        dict_bst1 = Dict_bst().from_list(arr1)
        arr2 = self.de_duplication(arr2)
        dict_bst2 = Dict_bst().from_list(arr2)
        self.assertEqual(dict_bst.mconcat(dict_bst1).mconcat(dict_bst2), dict_bst.mconcat(dict_bst1.mconcat(dict_bst2)))

if __name__ == '__main__':
    unittest.main()