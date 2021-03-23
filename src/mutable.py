# editor: Liu Fen
# ID in HDU: 202320050

import BSTree
import math
from functools import reduce

Node = BSTree.Node
BSTree = BSTree.BSTree

class Dict_bst(BSTree):
    def __init__(self, *args):
        """Initialzes tree the same as as BST"""
        BSTree.__init__(self, *args)

    # 1. add a new element
    def insert(self, key, value, *args):
        BSTree.insert(self, key, value, *args)

    # 2. remove an element
    def delete(self, key):
        BSTree.delete(self, key)

    # 3. size
    def size(self, *args):
        return BSTree.get_element_count(self, *args)

    # 4. conversion from and to python lists
    def from_list(self, list):
        for i in range(len(list)):
            self.insert(i, list[i])

    def to_list(self):
        return self.levelorder()

    # 5. find element by specific predicate
    def find_key(self, key, *args):
        return BSTree.get_node(self, key, *args)

    def find_value(self, value, *args):
        return BSTree.get_node1(self, value, *args)

    # 6. filter data structure by specific predicate
    def key_is_odd(self, node):
        return node.key % 2 == 1

    def value_is_odd(self, node):
        return node.value % 2 == 1

    def filter_func(self, func):
        list = self.to_list()
        newlist = filter(func, list)
        for i in newlist:
            self.delete(i.key)

    # 7. map structure by specific function
    def square(self, node):
        return node.key ** 2, node.value ** 2

    def map_func(self, func):
        list = self.to_list()
        newlist = map(func, list)
        dict_bst = BSTree()
        for i in newlist:
            dict_bst.insert(i[0], i[1])
        return dict_bst

    # 8. reduce – process structure elements to build a return value by specific functions
    def add(self, node1, node2) :
        return Node(node1.key+node2.key, node1.value+node2.value)

    def reduce_func(self, func):
        list = self.to_list()
        sum = reduce(func, list)
        return sum

    # 9. iterator
    def __iter__(self, root: Node):
        # Stack for the recursion simulation
        self.stack = []
        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)
        # print(self.stack)
        return self.stack

    def _leftmost_inorder(self, root):
        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        if not hasattr(self, "stack"):
            raise StopIteration
        topmost_node = self.stack.pop()
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    # 10. mempty and mconcat
    def mempty(self):
        self.Root = None
        return self.Root


    def mconcat(self, a):
        if self.Root == None:
            return a
        elif a.Root == None:
            return self
        else:
            ls1 = a.to_list()
            for i in ls1:
                self.insert(i.key, i.value)
            return self


