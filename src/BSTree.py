# editor: Liu Fen
# ID in HDU: 202320050

import collections
from collections.abc import Iterable
import numpy as np
import operator

class Node:
    """Represents a node of a binary tree"""
    def __init__(self,key,value):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = value
        # modify
        self.key1 = []
        if type(self.key) == type("abc"):
            for i in self.key:
                s = ord(i)
                self.key1.append(s)
            self.key1 = np.array(self.key1)
            # self.key1 = np.fromstring(self.key, dtype=np.uint8)
        elif type(self.key) == type(1):
            self.key1.append(self.key)
            self.key1 = np.array(self.key1)
        # print(self.key1)

    def __next__(self):
        return self

    def __iter__(self):
        return self
    # modify
    def __gt__(self, other):
        l1 = len(self.key1)
        l2 = len(other.key1)
        if l1 > l2:
            return True
        elif l1 == l2:
            flag = False
            for i in range(l1):
                if self.key1[i] == other.key1[i]:
                    continue
                elif self.key1[i] < other.key1[i]:
                    break
                elif self.key1[i] > other.key1[i]:
                    flag = True
                    break
            return flag
        else:  return False
    def __eq__(self, other):
        if other == None: return None
        l1 = len(self.key1)
        l2 = len(other.key1)
        if l1 != l2: return False
        elif all(self.key1==other.key1) is True:
            return True
        else: return False
    def __lt__(self, other):
        l1 = len(self.key1)
        l2 = len(other.key1)
        if l1 < l2:
            return True
        elif l1 == l2:
            flag = False
            for i in range(l1):
                if self.key1[i] == other.key1[i]:
                    continue
                elif self.key1[i] > other.key1[i]:
                    break
                elif self.key1[i] < other.key1[i]:
                    flag = True
                    break
            return flag
        else:
            return False

class BSTree:
    """
    BSTree implements an unbalanced Binary Search Tree.
    A Binary Search Tree is an ordered node based tree key structure
    in which each node has at most two children.
    Constructors:
    BSTree() -> Creates a new empty Binary Search Tree
    BSTree(seq) -> Creates a new Binary Search Tree from the elements in sequence [(k1,v1),(k2,v2),...,(kn,vn)]
    """
    def __init__(self,*args):

        self.Root = None

        if len(args) == 1:
            if isinstance(args[0],Iterable): # collections.
                for x in args[0]:
                    self.insert(x[0],x[1])
            else:
                raise TypeError(str(args[0]) + " is not iterable")

    def preorder(self,*args):
        """
        T.preorder(...) -> Sequence. Produces a sequence of the Nodes
        in T, obtained in preorder.
        """
        if len(args) == 0:
            elements = []
            node = self.Root
        else:
            node = args[0]
            elements = args[1]

        elements.append(node)

        if node.left:
            self.preorder(node.left,elements)
        if node.right:
            self.preorder(node.right,elements)

        return elements

    def inorder(self,*args):
        """
        T.inorder(...) -> Sequence. Produces a sequence of the Nodes
        in T, obtained in inorder.
        """
        if len(args) == 0:
            elements = []
            node = self.Root
        else:
            node = args[0]
            elements = args[1]

        if node.left:
            self.inorder(node.left,elements)

        elements.append(node)

        if node.right:
            self.inorder(node.right,elements)

        return elements

    def postorder(self,*args):
        """
        T.postorder(...) -> Sequence. Produces a sequence of the Nodes
        in T, obtained in postorder.
        """
        if len(args) == 0:
            elements = []
            node = self.Root
        else:
            node = args[0]
            elements = args[1]

        if node.left:
            self.postorder(node.left,elements)

        if node.right:
            self.postorder(node.right,elements)

        elements.append(node)

        return elements

    def levelorder(self):
        """
        T.levelorder(...) -> Sequence. Produces a sequence of the Nodes
        in T, obtained in levelorder.
        """
        q = collections.deque()
        q.appendleft(self.Root)
        lst = []
        while len(q):  #  != 0
            removed = q.pop()
            lst.append(removed)
            visit = self.get_node(removed.key,self.Root)
            if visit.left:
                q.appendleft(visit.left)
            if visit.right:
                q.appendleft(visit.right)
        return lst

    def get_node(self,key,*args):
        """
        T.get_node(key,...) -> Node. Produces the Node in T with key
        attribute key. If there is no such node, produces None.
        """
        if len(args) == 0:
            start = self.Root
        else:
            start = args[0]
        if not start:
            return None
        a = Node(key, 1)
        if a == start:
            return start
        elif a > start:
            return self.get_node(key,start.right)
        else:
            return self.get_node(key,start.left)

    def get_node1(self,value,*args):
        """
        T.get_node(value,...) -> Node. Produces the Node in T with value
        attribute value. If there is no such node, produces None.
        """
        if len(args) == 0:
            start = self.Root
        else:
            start = args[0]
        if not start:
            return None
        if value == start.value:
            return start
        return self.get_node1(value,start.left)
        return self.get_node1(value,start.right)

    def insert(self,key,value,*args):
        """
        T.insert(key,value...) <==> T[key] = value. Inserts
        a new Node with key attribute key and value attribute
        value into T.
        """
        if not self.Root:
            self.Root = Node(key,value)
            #print(type(self.Root))
        elif len(args) == 0:
            if not self.get_node(key,self.Root):
                self.insert(key,value,self.Root)
        else:
            child = Node(key,value)
            parent = args[0]
            #print(args[0].key, args[0].value)
            if child > parent:
                if not parent.right:
                    parent.right = child
                    child.parent = parent
                else:
                    self.insert(key,value,parent.right)
            else:
                if not parent.left:
                    parent.left = child
                    child.parent = parent
                else:
                    self.insert(key,value,parent.left)

    def get_element_count(self,*args):
        """
        T.get_element_count(...) -> Nat. Produces the number of elements
        in T.
        """
        if len(args) == 0:
            node = self.Root
        else:
            node = args[0]

        left = 0
        right = 0

        if node:
            if node.left:
                left = self.get_element_count(node.left)
            if node.right:
                right = self.get_element_count(node.right)

            return 1 + left + right
        else:
            return 0

    def _delete_leaf(self,node):
        """
        T._delete_leaf(node). Deletes node from T, treating it as a leaf.
        """
        par_node = node.parent
        if par_node:
            if par_node.left == node:
                par_node.left = None
            else:
                par_node.right = None

            del node

    def _delete_leaf_parent(self,node):
        """
        T._delete_leaf_parent(node). Deletes node from T, treating it
        as a node with only one child.
        """
        par_node = node.parent

        if node == self.Root:
            if node.right:
                self.Root = node.right
                node.right = None
            else:
                self.Root = node.left
                node.left = None

        else:
            if par_node.right == node:
                if node.right:
                    par_node.right = node.right
                    par_node.right.parent = par_node
                    node.right = None
                else:
                    par_node.right = node.left
                    par_node.right.parent = par_node
                    node.left = None
            else:
                if node.right:
                    par_node.left = node.right
                    par_node.left.parent = par_node
                    node.right = None
                else:
                    par_node.left = node.left
                    par_node.left.parent = par_node
                    node.left = None
        del node

    def _switch_nodes(self,node1,node2):
        """
        T._switch_nodes(node1,node2). Switches positions
        of node1 and node2 in T.
        """
        switch1 = node1
        switch2 = node2
        temp_key = switch1.key
        tmp_key1 = switch1.key1
        temp_value = switch1.value

        if switch1 == self.Root:
            self.Root.key = node2.key
            self.Root.key1 = node2.key1
            self.Root.value = node2.value
            switch2.key = temp_key
            switch2.key1 = temp_key1
            switch2.value = temp_value

        elif switch2 == self.Root:
            switch1.key = self.Root.key
            switch1.key1 = self.Root.key1
            self.Root.key = temp_key
            self.Root.key1 = temp_key1
            self.Root.value = temp_value
        else:
            switch1.key = node2.key
            switch1.key1 = node2.key1
            switch1.value = node2.value
            switch2.key = temp_key
            switch2.key1 = temp_key1
            switch2.value = temp_value

    def get_height(self,*args):
        """
        T.get_height(...) -> Nat. Produces the height of T, defined
        as one added to the height of the tallest subtree.
        """
        if len(args) == 0:
            node = self.Root
        else:
            node = args[0]

        if not node or (not node.left and not node.right):
            return 0
        else:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_max(self,*args):
        """
        T.get_max(...) -> Node. Produces the Node that has the maximum
        key attribute in T.
        """
        if len(args) == 0:
            node = self.Root
        else:
            node = args[0]

        if not node.right:
            return node
        else:
            return self.get_max(node.right)

    def get_min(self,*args):
        """
        T.get_min(...) -> Node. Produces the Node that has the minimum
        key attribute in T.
        """
        if len(args) == 0:
            node = self.Root
        else:
            node = args[0]

        if not node.left:
            return node
        else:
            return self.get_min(node.left)

    def _delete_node(self,node):
        """
        T._delete_node(node). Deletes node from T, treating it as
        a node with two children.
        """
        if self.get_height(node.left) > self.get_height(node.right):
            to_switch = self.get_max(node.left)
            self._switch_nodes(node,to_switch)

            if not (to_switch.right or to_switch.left):
                to_delete = self.get_max(node.left)
                self._delete_leaf(to_delete)
            else:
                to_delete = self.get_max(node.left)
                self._delete_leaf_parent(to_delete)
        else:
            to_switch = self.get_min(node.right)
            self._switch_nodes(node,to_switch)

            if not (to_switch.right or to_switch.left):
                to_delete = self.get_min(node.right)
                self._delete_leaf(to_delete)
            else:
                to_delete = self.get_min(node.right)
                self._delete_leaf_parent(to_delete)

    def delete(self,key):
        """T.delete(key) <==> del T[key]. Deletes the node
        with key attribute key from T.
        """
        node = self.get_node(key,self.Root)

        if node:
            if not (node.left or node.right):
                self._delete_leaf(node)

            elif not (node.left and node.right):
                self._delete_leaf_parent(node)

            else:
                self._delete_node(node)


