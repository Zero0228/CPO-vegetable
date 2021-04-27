# editor: Zhuo lin
from typing import TypeVar, Generic, List, Iterator, Callable, Generator

class TreeNode:
	def __init__(self,key,val,left=None,right=None):	
		self.key = key
		self.val = val
		self.leftChild = left
		self.rightChild = right

key_type = TypeVar(str, int, float)
val_type = TypeVar(None, str, int, float)
node_type = TypeVar(TreeNode)

def size(bst: node_type) -> int:
    if bst is None:
        return 0
    else:
        return 1 + size(bst.leftChild) + size(bst.rightChild)

def insert(bst: node_type, key: key_type, val: val_type) -> node_type:
    if key == None or val == None:
        return False
    if bst is None:
        bst = TreeNode(key,val)
    else:
        if type(key) is str:
            key_num = 0
            for i in range(len(key)):
                key_num = key_num + ord(key[i])
        else:
            key_num = key
        if type(bst.key) is str:
            bstkey_num = 0
            for i in range(len(bst.key)):
                bstkey_num = bstkey_num + ord(bst.key[i])
        else:
            bstkey_num = bst.key
        if key_num <= bstkey_num:
            if bst.leftChild is None:
                bst.leftChild = TreeNode(key,val)
            else:
                insert(bst.leftChild,key,val)
        else:
            if bst.rightChild is None:
                bst.rightChild = TreeNode(key,val)
            else:
                insert(bst.rightChild,key,val)
    return bst

def get(bst: node_type, key: key_type) -> node_type:
    if bst is None:
        return None
    elif key ==  bst.key:
        return bst
    elif key < bst.key:
        return get(bst.leftChild,key)
    else:
        return get(bst.rightChild,key)

def find(bst: node_type, key: key_type) -> val_type:
    if get(bst,key) == None:
        return False
    else:
        return get(bst,key).val

def parent(bst: node_type, key: key_type) -> node_type:
    if bst is None or bst.key == key:
        return None
    elif key ==  bst.leftChild.key or key ==  bst.rightChild.key:
        return bst
    elif key < bst.key:
        return parent(bst.leftChild,key)
    else:
        return parent(bst.rightChild,key)

def indict(bst: node_type, k: key_type, v: val_type) -> bool:
    if find(bst,k) == v:
        return True
    else:
        return False

def delete(bst: node_type, key: key_type) -> None:
    n = get(bst,key)
    if n == None:
        raise AttributeError("The element does not exist")
    p = parent(bst,key)
    if n.leftChild is None:
        if n == p.leftChild:
            p.leftChild = n.rightChild
        else:
            p.rightChild = n.rightChild
        del n
    elif n.rightChild is None:
        if n == p.leftChild:
            p.leftChild = n.leftChild
        else:
            p.rightChild = n.leftChild
    else:
        pre = n.rightChild
        if pre.leftChild is None:
            n.key = pre.key
            n.val = pre.val
            n.rightChild = pre.rightChild
            del pre
        else:
            temp = pre.leftChild
            while temp.leftChild is not None:
                pre = temp
                temp = temp.leftChild
            n.key = temp.key
            n.val = temp.val
            pre.leftChild = temp.rightChild
            del temp

def tolist(bst: node_type) -> list:
    res = []
    def tolist_loop(bst,ans):
        if bst is not None:
            ans.append(bst.key)
            ans.append(bst.val)
            ans = tolist_loop(bst.leftChild,ans)
            ans = tolist_loop(bst.rightChild,ans)
        return ans
    return tolist_loop(bst, res)

def fromlist(lst: list) -> node_type:
    bst = None
    if len(lst) == 0:
        return None
    elif len(lst) % 2 == 1:
        return False
    else:
        for i in range(0,len(lst),2):
            bst = insert(bst,lst[i],lst[i+1])
        return bst

def map(bst: node_type, f: Generator[str, int, float]) -> None:
    if bst is not None:
        bst.val = f(bst.val) 
        map(bst.leftChild,f)
        map(bst.rightChild,f)

def func(bst: node_type, f: Generator[str, int, float]) -> int:
    ans = [0]
    def func_loop(bst,f,ans):
        if bst is not None:
            ans[0] = f(ans[0], bst.val)
            func_loop(bst.leftChild,f,ans)
            func_loop(bst.rightChild,f,ans)
        return ans
    return func_loop(bst,f,ans)[0]

def filter(tree: node_type, rule: Generator[str, int, float]) -> node_type:
    bst = None
    def filter_loop(bst,current,rule):
        if current is not None:
            if rule(current.key) is False:
                bst = insert(bst,current.key,current.val)
            bst = filter_loop(bst,current.leftChild,rule)
            bst = filter_loop(bst,current.rightChild,rule)
        return bst
    return filter_loop(bst, tree, rule)

def mconcat(bst1: node_type, bst2: node_type) -> node_type:
    lst1 = tolist(bst1)
    lst2 = tolist(bst2)
    lst = lst1 + lst2
    return fromlist(lst)

def mempty() -> None:
    return None

def iterator(bst: node_type) -> list:
    return [tolist(bst), 0]

def next_item(it_lst: list) -> node_type:
    lst = it_lst[0]
    cur = it_lst[1]
    def foo():
        nonlocal cur
        if cur >= len(lst) or lst == []: raise StopIteration
        tmp = lst[cur]
        cur = cur + 1
        it_lst[1] = it_lst[1] + 1
        return tmp
    return foo