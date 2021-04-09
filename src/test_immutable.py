# editor: Zhuo lin

import unittest
from hypothesis import given
import hypothesis.strategies as st
from immutable import *

class TestImmutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(size(None), 0)
        self.assertEqual(size(TreeNode(3,'a')), 1)
        self.assertEqual(size(TreeNode(3,'a',TreeNode(2,'b'))), 2)
        self.assertEqual(size(TreeNode(3,'a',TreeNode(2,'b'),TreeNode(5,'c'))), 3)
    
    def test_insert(self):
        self.assertEqual(insert(None,3,'a').key, 3)
        self.assertEqual(insert(None,3,'a').val, 'a')
        self.assertEqual(insert(TreeNode(3,'a'),2,'b').key,3)
        self.assertEqual(insert(TreeNode(3,'a'),2,'b').val,'a')
        self.assertEqual(insert(TreeNode(3,'a'),2,'b').leftChild.key,2)
        self.assertEqual(insert(TreeNode(3,'a'),2,'b').leftChild.val,'b')
        self.assertEqual(insert(TreeNode(3,'a'),5,'c').key,3)
        self.assertEqual(insert(TreeNode(3,'a'),5,'c').val,'a')
        self.assertEqual(insert(TreeNode(3,'a'),5,'c').rightChild.key,5)
        self.assertEqual(insert(TreeNode(3,'a'),5,'c').rightChild.val,'c')

    def test_find(self):
        T = TreeNode(3,'a',TreeNode(2,'b'),TreeNode(5,'c'))
        self.assertEqual(find(T,3),'a')
        self.assertEqual(find(T,2),'b')
        self.assertEqual(find(T,5),'c')
        self.assertEqual(find(T,6),False)
        
    def test_indict(self):
        T = TreeNode(3,'a',TreeNode(2,'b'),TreeNode(5,'c'))
        self.assertEqual(indict(T,2,'b'),True)

    def test_delete(self):
        T = TreeNode(3,'a',TreeNode(2,'b'),TreeNode(5,'c'))
        self.assertEqual(indict(T,2,'b'),True)
        delete(T,2)
        self.assertEqual(indict(T,2,'b'),False)

    def test_tolist(self):
        T = TreeNode(3,'a',TreeNode(2,'b'),TreeNode(5,'c'))
        ans = []
        self.assertEqual(tolist(T,ans),['a','b','c'])

    def test_fromlist(self):
        lst = ['a','b','c']
        T = fromlist(lst)
        self.assertEqual(T.val, 'a')
        self.assertEqual(T.rightChild.val,'b')
        self.assertEqual(T.rightChild.rightChild.val,'c')
        lst2 = []
        self.assertEqual(fromlist(lst2),None)

    def test_map(self):
        T = TreeNode(3,4,TreeNode(2,6),TreeNode(5,7))
        def f(x):
            return x*2
        map(T,f)
        self.assertEqual(T.key, 3)
        self.assertEqual(T.val, 8)
        lc = T.leftChild
        rc = T.rightChild
        self.assertEqual(lc.key,2)
        self.assertEqual(lc.val,12)
        self.assertEqual(rc.key,5)
        self.assertEqual(rc.val,14)

    def test_func(self):
        T = TreeNode(3,4,TreeNode(2,6),TreeNode(5,7))
        s = [0]
        def fsum(x,s):
            return s+x
        self.assertEqual(func(T,fsum,s)[0],17)

    def test_filter(self):
        T = TreeNode(3,4,TreeNode(2,6),TreeNode(5,7))
        def r(key):
            if key % 2 == 0:
                return True
            else:
                return False
        filter(T,T,r)
        self.assertEqual(T.leftChild,None)

    def test_mconcat(self):
        T1 = TreeNode(3,4,TreeNode(2,6),TreeNode(5,7))
        T2 = TreeNode(1,8)
        mconcat(T2,T1)
        lc = T1.leftChild
        self.assertEqual(lc.leftChild.key,1)
        self.assertEqual(lc.leftChild.val,8)

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        ans = []
        self.assertEqual(tolist(fromlist(a),ans), a)
    
    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        a = fromlist(lst)
        self.assertEqual(mconcat(mempty(), a), a)
        self.assertEqual(mconcat(a, mempty()), a)

    def test_iter(self):
        T = TreeNode(3,'a',TreeNode(2,'b'),TreeNode(5,'c'))
        iteration(T)
        ls = None
        self.assertRaises(StopIteration, lambda: next(T,iteration(T)))

if __name__ == '__main__':
    unittest.main()