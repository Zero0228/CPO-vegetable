# editor: Zhuo lin

class TreeNode:
	def __init__(self,key,val,left=None,right=None):	
		self.key = key
		self.val = val
		self.leftChild = left
		self.rightChild = right

def size(bst):
    if bst is None:
        return 0
    else:
        return 1 + size(bst.leftChild) + size(bst.rightChild)

def insert(bst,key,val):
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

def get(bst,key):
    if bst is None:
        return None
    elif key ==  bst.key:
        return bst
    elif key < bst.key:
        return get(bst.leftChild,key)
    else:
        return get(bst.rightChild,key)

def find(bst,key):
    if get(bst,key) == None:
        return False
    else:
        return get(bst,key).val

def parent(bst,key):
    if bst is None or bst.key == key:
        return None
    elif key ==  bst.leftChild.key or key ==  bst.rightChild.key:
        return bst
    elif key < bst.key:
        return parent(bst.leftChild,key)
    else:
        return parent(bst.rightChild,key)

def indict(bst,k,v):
    if find(bst,k) == v:
        return True
    else:
        return False

def delete(bst,key):
    n = get(bst,key)
    if n == None:
        return False
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

def tolist(bst):
    res = []
    def tolist_loop(bst,ans):
        if bst is not None:
            ans.append(bst.key)
            ans.append(bst.val)
            ans = tolist_loop(bst.leftChild,ans)
            ans = tolist_loop(bst.rightChild,ans)
        return ans
    return tolist_loop(bst, res)

def fromlist(lst):
    bst = None
    if len(lst) == 0:
        return None
    elif len(lst) % 2 == 1:
        return False
    else:
        for i in range(0,len(lst),2):
            bst = insert(bst,lst[i],lst[i+1])
        return bst

def map(bst,f):
    if bst is not None:
        bst.val = f(bst.val) 
        map(bst.leftChild,f)
        map(bst.rightChild,f)

def func(bst,f):
    ans = [0]
    def func_loop(bst,f,ans):
        if bst is not None:
            ans[0] = f(ans[0], bst.val)
            func_loop(bst.leftChild,f,ans)
            func_loop(bst.rightChild,f,ans)
        return ans
    return func_loop(bst,f,ans)[0]

def filter(tree,rule):
    bst = None
    def filter_loop(bst,current,rule):
        if current is not None:
            if rule(current.key) is False:
                bst = insert(bst,current.key,current.val)
            bst = filter_loop(bst,current.leftChild,rule)
            bst = filter_loop(bst,current.rightChild,rule)
        return bst
    return filter_loop(bst, tree, rule)

def mconcat(bst1,bst2):
    lst1 = tolist(bst1)
    lst2 = tolist(bst2)
    lst = lst1 + lst2
    return fromlist(lst)

def mempty():
    return None

def iterator(bst):
    lst = tolist(bst)
    cur = 0
    def foo():
        nonlocal cur
        if cur >= len(lst) or lst == []: raise StopIteration
        tmp = lst[cur]
        cur = cur + 1
        return tmp
    return foo