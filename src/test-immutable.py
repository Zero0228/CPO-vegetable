# editor: Zhuo lin

import unittest
from immutable import *

class TestMutableList(unittest.TestCase):
    def test_size(self):
        T = BinarySearchTree()
        self.assertEqual(T.size, 0)
        insert(T,3,4)
        self.assertEqual(T.size, 1)
        insert(T,3,4)
        self.assertEqual(T.size, 2)
    
    def test_insert(self):
        T = BinarySearchTree()
        insert(T,3,4)
        self.assertEqual(T.root.key, 3)
        self.assertEqual(T.root.payload, 4)
        insert(T,2,6)
        insert(T,5,7)
        lc = T.root.leftChild
        rc = T.root.rightChild
        self.assertEqual(lc.key,2)
        self.assertEqual(lc.payload,6)
        self.assertEqual(rc.key,5)
        self.assertEqual(rc.payload,7)

    def test_find(self):
        T = BinarySearchTree()
        insert(T,3,4)
        self.assertEqual(find(T,3),4)
        self.assertEqual(find(T,2),None)

    def test_delete(self):
        T = BinarySearchTree()
        insert(T,3,4)
        insert(T,2,6)
        insert(T,5,7)
        self.assertEqual(indict(T,2,6),True)
        delete(T,2)
        self.assertEqual(indict(T,2,6),False)

    def test_tolist(self):
        T = BinarySearchTree()
        insert(T,3,4)
        insert(T,2,6)
        insert(T,5,7)
        ans = []
        self.assertEqual(tolist(T,T.root,ans),[3,4,2,6,5,7])

    def test_fromlist(self):
        lst = [3,4,2,6,5,7]
        T = BinarySearchTree()
        fromlist(T,lst)
        self.assertEqual(T.root.key, 3)
        self.assertEqual(T.root.payload, 4)
        lc = T.root.leftChild
        rc = T.root.rightChild
        self.assertEqual(lc.key,2)
        self.assertEqual(lc.payload,6)
        self.assertEqual(rc.key,5)
        self.assertEqual(rc.payload,7)
        lst2 = [3,4,2,6,5]
        T2 = BinarySearchTree()
        self.assertEqual(fromlist(T2,lst2),False)

    def test_map(self):
        T = BinarySearchTree()
        insert(T,3,4)
        insert(T,2,6)
        insert(T,5,7)
        def f(x):
            return x*2
        map(T,T.root,f)
        self.assertEqual(T.root.key, 3)
        self.assertEqual(T.root.payload, 8)
        lc = T.root.leftChild
        rc = T.root.rightChild
        self.assertEqual(lc.key,2)
        self.assertEqual(lc.payload,12)
        self.assertEqual(rc.key,5)
        self.assertEqual(rc.payload,14)

    def test_reduce(self):
        T = BinarySearchTree()
        insert(T,3,4)
        insert(T,2,6)
        insert(T,5,7)
        s = [0]
        def fsum(x,s):
            return s+x
        self.assertEqual(r(T,T.root,fsum,s)[0],17)

    def test_combine(self):
        T1 = BinarySearchTree()
        insert(T1,3,4)
        insert(T1,2,6)
        insert(T1,5,7)
        T2 = BinarySearchTree()
        insert(T2,1,8)
        combine(T2,T2.root,T1)
        lc = T1.root.leftChild
        self.assertEqual(lc.leftChild.key,1)
        self.assertEqual(lc.leftChild.payload,8)

    def test_iter(self):
        T = BinarySearchTree()
        insert(T,3,4)
        insert(T,2,6)
        insert(T,5,7)
        iteration(T,T.root)
        ls = BinarySearchTree()
        self.assertRaises(StopIteration, lambda: next(T,iteration(T,T.root)))

if __name__ == '__main__':
    unittest.main()