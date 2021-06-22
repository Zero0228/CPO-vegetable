# editor: Liu Fen
# ID in HDU: 202320050

import BSTree
import math
from functools import reduce
from typing import TypeVar, Generic, List, Iterator, Callable, Generator, Union, Optional, Any

Node = BSTree.Node
BST = BSTree.BSTree
T1 = TypeVar('T1', str, int, float)
T2 = TypeVar('T2', None, str, int, float)


class Dict_bst(BST):
    def __init__(self, *args) -> None:
        BST.__init__(self, *args)

    # 1. add a new element
    def insert(self, key: T1, value: T2, *args: Union[Node, None]) -> None:
        BST.insert(self, key, value, *args)

    # 2. remove an element
    def delete(self, key: T1) -> None:
        BST.delete(self, key)

    # 3. size
    def size(self, *args: Union[Node, None]) -> int:
        return BST.get_element_count(self, *args)

    # 4. conversion from and to python lists
    def from_list(self, list) -> 'Dict_bst':
        if list == []: return self
        else:
            for i in list:
                self.insert(i.key, i.value)
            return self

    def to_list(self) -> List:
        if self.Root == None: return []
        else: return self.levelorder()

    # 5. find element by specific predicate
    def find_key(self, key: T1, *args: Optional[Node]) -> Optional[Node]:
        return BST.get_node(self, key, *args)

    def find_value(self, value: T2, *args: Optional[Node]) -> Optional[Node]:
        return BST.get_node1(self, value, *args)

    # 6. filter data structure by specific predicate
    def filter_func(self, func: Callable) -> None:
        list = self.to_list()
        newlist = filter(func, list)
        for i in newlist:
            self.delete(i.key)

    # 7. map structure by specific function
    def map_func(self, func: Callable) -> BST[Any, Any]:
        list = self.to_list()
        newlist = map(func, list)
        dict_bst = BST() # type: BST
        for i in newlist:
            dict_bst.insert(i[0], i[1])
        return dict_bst

    # 8. reduce – process structure elements to build a return value by specific functions
    def reduce_func(self, func: Callable) -> T1:
        list = self.to_list()
        sum = reduce(func, list)
        return sum

    # 9. iterator
    def __iter__(self) -> Iterator:
        return iter(self.to_list())

    def next(self) -> Iterator[Any]:
        if self.Root == None:
            raise StopIteration
        else:
            return iter(self.to_list())

    # 10. mempty and mconcat
    def mempty(self) -> 'Dict_bst':
        self.Root = None
        return self

    def mconcat(self, a: 'Dict_bst') -> 'Dict_bst':
        if self.Root == None:
            return a
        elif a.Root == None:
            return self
        else:
            ls1 = a.to_list()
            for i in ls1:
                self.insert(i.key, i.value)
            return self

