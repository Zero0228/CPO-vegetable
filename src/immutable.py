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
    # check whether the tree has the root
    # if true, search the tree and insert; else, build a root for it
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
    # check whether the tree has the root
    # if true, search the tree; else, return none
    if bst is None:
        return None
    elif key ==  bst.key:
        return bst
    elif key < bst.key:
        return get(bst.leftChild,key)
    else:
        return get(bst.rightChild,key)

def find(bst,key):
    # check whether the tree has the root
    # if true, search the tree; else, return none
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
    # search whether there is a key in the map
    if find(bst,k) == v:
        return True
    else:
        return False

def delete(bst,key):
    # delete the element by key value
    n = get(bst,key)
    p = parent(bst,key)
    if n == None:
        return False
    elif n.leftChild is None:
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

def tolist(bst,ans):
    # Conversion to built-in list in preorder 
    if bst is not None:
        ans.append(bst.key)
        ans.append(bst.val)
        tolist(bst.leftChild,ans)
        tolist(bst.rightChild,ans)
    return ans

def fromlist(lst):
    # Conversion from built-in list in preorder
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
    # Conversion to built-in list in preorder 
    if bst is not None:
        bst.val = f(bst.val) 
        map(bst.leftChild,f)
        map(bst.rightChild,f)

def func(bst,f,ans):
    # process structure elements to build a return value by specific functions
    if bst is not None:
        ans[0] = f(ans[0], bst.val)
        func(bst.leftChild,f,ans)
        func(bst.rightChild,f,ans)
    return ans

def filter(bst,current,rule):
    if current is not None:
        if rule(current.key) is False:
            bst = insert(bst,current.key,current.val)
        bst = filter(bst,current.leftChild,rule)
        bst = filter(bst,current.rightChild,rule)
    return bst

def mconcat(bst,T):
    # add current tree to T 
    if bst is None:
        return T
    else:
        if T is None:
            return mconcat(T,bst)
        k = bst.key
        v = bst.val
        insert(T,k,v)
        mconcat(bst.leftChild,T)
        mconcat(bst.rightChild,T)

def mempty():
    return None

def iteration(bst):
    # Stack for the recursion simulation
    stack = []
    # Remember that the algorithm starts with a call to the helper function
    # with the root node as the input
    _leftmost_inorder(bst,stack)
    return stack

def _leftmost_inorder(bst,stack):
    # For a given node, add all the elements in the leftmost branch of the tree
    # under it to the stack.
    while bst:
        stack.append(bst)
        bst = bst.leftChild

def next(bst,stack):
    if not hasattr(bst, "stack"):
        raise StopIteration
    topmost_node = stack.pop()
    if topmost_node.rightChild:
        _leftmost_inorder(bst,topmost_node.rightChild,stack)
    return topmost_node

def hasNext(bst,stack) -> bool:
        return len(stack) > 0