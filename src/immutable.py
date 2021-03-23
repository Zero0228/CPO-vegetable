# editor: Zhuo lin

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

class TreeNode:
	def __init__(self,key,val,left=None,right=None,parent=None):	
		self.key = key
		self.payload = val
		self.leftChild = left
		self.rightChild = right
		self.parent = parent

	def hasLeftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild

	def isLeftChild(self):
		return self.parent and self.parent.leftChild == self

	def isRightChild(self):
		return self.parent and self.parent.rightChild == self

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.rightChild or self.leftChild)

	def hasAnyChildren(self):
		return self.rightChild or self.leftChild

	def hasBothChildren(self):
		return self.rightChild and self.leftChild

	def replaceNodeData(self,key,value,lc,rc):
		self.key = key
		self.payload = value
		self.leftChild = lc
		self.rightChild = rc
		if self.hasLeftChild():
			self.leftChild.parent = self
		if self.hasRightChild():
			self.rightChild.parent = self

def put(bst,key,val):
    # check whether the tree has the root
    # if true, search the tree and insert; else, build a root for it
    if bst.root:
        _put(bst,key,val,bst.root)
    else:
        bst.root = TreeNode(key,val) 
    bst.size = bst.size + 1

def _put(bst,key,val,currentNode):
    # search the tree from the currentNode and insert
    if key < currentNode.key:
        if currentNode.hasLeftChild():
            _put(bst,key,val,currentNode.leftChild)
        else:
            currentNode.leftChild = TreeNode(key,val,parent=currentNode)
    else:
        if currentNode.hasRightChild():
            _put(bst,key,val,currentNode.rightChild)
        else:
            currentNode.rightChild = TreeNode(key,val,parent=currentNode)

def get(bst,key):
    # check whether the tree has the root
    # if true, search the tree; else, return none
    if bst.root:
        res = _get(bst,key,bst.root)
        if res:
            return res.payload
        else:
            return None
    else:
        return None

def _get(bst,key,currentNode):
    # search the tree from the currentNode
    if not currentNode:
        return None
    elif currentNode.key == key:
        return currentNode
    elif key < currentNode.key:
        return _get(bst,key,currentNode.leftChild)
    else:
        return _get(bst,key,currentNode.rightChild)

def insert(bst,k,v):
    # insert the new element(k:v)
    put(bst,k,v)

def find(bst,key):
    # search the map by the key
    return get(bst,key)

def indict(bst,k,v):
    # search whether there is a key in the map
    if get(bst,k) == v:
        return True
    else:
        return False

def delete(bst,key):
    # delete the element by key value
    n = _get(bst,key,bst.root)
    p = n.parent
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
            n.payload = pre.payload
            n.rightChild = pre.rightChild
            del pre
        else:
            temp = pre.leftChild
            while temp.leftChild is not None:
                pre = temp
                temp = temp.leftChild
            n.key = temp.key
            n.payload = temp.payload
            pre.leftChild = temp.rightChild
            del temp

def tolist(bst,currentNode,ans):
    # Conversion to built-in list in preorder 
    if currentNode is not None:
        ans.append(currentNode.key)
        ans.append(currentNode.payload)
        tolist(bst,currentNode.leftChild,ans)
        tolist(bst,currentNode.rightChild,ans)
    return ans

def fromlist(bst, list):
    # Conversion from built-in list in preorder
    if len(list) % 2 == 0:
        for i in range(0,len(list),2):
            insert(bst,list[i], list[i+1])
    else:
        return False

def map(bst,currentNode,f):
    # Conversion to built-in list in preorder 
    if currentNode is not None:
        currentNode.payload = f(currentNode.payload) 
        map(bst,currentNode.leftChild,f)
        map(bst,currentNode.rightChild,f)

def r(bst,currentNode,f,ans):
    # process structure elements to build a return value by specific functions
    if currentNode is not None:
        ans[0] = f(ans[0], currentNode.payload)
        r(bst,currentNode.leftChild,f,ans)
        r(bst,currentNode.rightChild,f,ans)
    return ans

def combine(bst,currentNode,T):
    # add current tree to T 
    if currentNode is not None:
        k = currentNode.key
        v = currentNode.payload
        insert(T,k,v)
        combine(bst,currentNode.leftChild,T)
        combine(bst,currentNode.rightChild,T)

def iteration(bst, currentNode):
    # Stack for the recursion simulation
    stack = []
    # Remember that the algorithm starts with a call to the helper function
    # with the root node as the input
    _leftmost_inorder(bst,currentNode,stack)
    return stack

def _leftmost_inorder(bst, currentNode,stack):
    # For a given node, add all the elements in the leftmost branch of the tree
    # under it to the stack.
    while currentNode:
        stack.append(currentNode)
        currentNode = currentNode.leftChild

def next(bst,stack):
    if not hasattr(bst, "stack"):
        raise StopIteration
    topmost_node = stack.pop()
    if topmost_node.rightChild:
        _leftmost_inorder(bst,topmost_node.rightChild,stack)
    return topmost_node

def hasNext(bst,stack) -> bool:
        return len(stack) > 0