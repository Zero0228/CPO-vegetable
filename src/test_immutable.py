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
        self.assertEqual(size(None), 0)
        self.assertEqual(size(TreeNode(3,'a')), 1)
        self.assertEqual(size(TreeNode(3,'a',TreeNode(2,None))), 2)
        tmp = TreeNode(3,'a',TreeNode("sadf",'b'),TreeNode(5,'c'))
        tmp = insert(tmp, "g", "g")
        self.assertEqual(size(tmp), 4)
    
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
        self.assertEqual(tolist(T,ans),[3, 'a', 2, 'b', 5, 'c'])

    def test_fromlist(self):
        lst = [3, 'a', 2, 'b', 5, 'c']
        T = fromlist(lst)
        self.assertEqual(T.val, 'a')
        self.assertEqual(T.leftChild.val,'b')
        self.assertEqual(T.rightChild.val,'c')
        lst2 = []
        self.assertEqual(fromlist(lst2),None)
        lst3 = [3, 'a', 2, 'b', 5]
        self.assertEqual(fromlist(lst3),False)

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
            return key % 2 == 0
        T_filter = None
        T_filter = filter(T_filter,T,r)
        self.assertEqual(T_filter.key,3)
        self.assertEqual(T_filter.val,4)
        self.assertEqual(T_filter.leftChild,None)
        self.assertEqual(T.leftChild.key,2)
        self.assertEqual(T.leftChild.val,6)
        self.assertEqual(T_filter.rightChild.key,5)
        self.assertEqual(T_filter.rightChild.val,7)

    def test_mconcat(self):
        T1 = TreeNode(3,4,TreeNode(2,6),TreeNode(5,7))
        T2 = TreeNode(1,8)
        mconcat(T2,T1)
        lc = T1.leftChild
        self.assertEqual(lc.leftChild.key,1)
        self.assertEqual(lc.leftChild.val,8)

    element = st.one_of(st.integers(),st.text(min_size=1))
    @given(st.lists(element))
    def test_from_list_to_list_equality(self, a):
        ans = []
        if len(a) % 2 == 1:
            self.assertEqual(fromlist(a), False)
        else:
            for i in range(0,len(a),2):
                for j in range(i+2,len(a),2):
                    if type(a[i]) is str:
                        ai_num = 0
                        for k in range(len(a[i])):
                            ai_num = ai_num + ord(a[i][k])
                    else:
                        ai_num = a[i]
                    if type(a[j]) is str:
                        aj_num = 0
                        for k in range(len(a[j])):
                            aj_num = aj_num + ord(a[j][k])
                    else:
                        aj_num = a[j]
                    if ai_num > aj_num:
                        a[i], a[j] = a[j], a[i]
                        a[i+1], a[j+1] = a[j+1], a[i+1]
            self.assertEqual(tolist(fromlist(a),ans), a)
    
    element = st.one_of(st.integers(),st.text(min_size=1))
    @given(st.lists(element))
    def test_monoid_identity(self, lst):
        if len(lst) % 2 == 1:
            self.assertEqual(fromlist(lst), False)
        else:
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