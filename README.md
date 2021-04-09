# CPO-vegetable

## Basic Information
> - ### title:  
>   &emsp;**Laboratory work 1**
> - ### list of group members:  
>   - **Liu Fen**
>       - ID in HDU: 202320050
>       - email: 962928173@qq.com
>   - **Zhuo Lin**
>       - ID in HDU: 202320058
>       - email: lynn_zhuolin@163.com
> - ### laboratory work number:  
>   &emsp;**6. Dictionary based on binary-tree**
> - ### variant description:  
>   &emsp;You need to check that your implementation correctly works with None value.  
>   &emsp;You need to implement functions/methods for getting/setting value by key. 
> - ### synopsis:
>   - Task division
>   - Design immutable version
>   - Design mutable version
>   - Conclusion
## Task division
> - **Zhuo Lin**: Implement and test the immutable versions.
> - **Liu Fen**: Implement and test the mutable versions.

## Design immutable version
> &emsp;In contrast to the use of class in the mutable version, the immutable version is implemented using static methods, passing object as parameter into the static methods to achieve a series of operations.

## Design mutable version
> &emsp;The key to designing mutable version is that you can directly change the value of an object at its original address while operating on it. In designing the mutable version we create a class directly so that all the operations can be implemented directly in the instance.

## Conclusion
> &emsp;The mutable version is more flexible and easier to use than the immutable version.
> 

## Update
> - **Zhuo Lin**: Check all functions in the immutable versions.
>                 Add property-based tests for from_list and to_list, all monoid properties (Associativity, Identity element) for immutable versions.
>                 Add filter for immutable.
         
> - **Liu Fen**:
> 2. Fix warnings:
> >     from collections.abc import Iterable
> 8. Remove key type restriction.
> In this part, I overloaded symbols, such as'>'/'=='/'<'(Node).
> >         def __gt__(self, other):
> >             l1 = len(self.key1)
> >             l2 = len(other.key1)
> >             if l1 > l2:
> >                 return True
> >             elif l1 == l2:
> >                 flag = False
> >                 for i in range(l1):
> >                     if self.key1[i] == other.key1[i]:
> >                         continue
> >                     elif self.key1[i] < other.key1[i]:
> >                         break
> >                     elif self.key1[i] > other.key1[i]:
> >                         flag = True
> >                         break
> >                 return flag
> >             else:  return False
> >             
> >             def __eq__(self, other):
> >                 if other == None: return None
> >                 l1 = len(self.key1)
> >                 l2 = len(other.key1)
> >                 if l1 != l2: return False
> >                 elif all(self.key1==other.key1) is True:
> >                     return True
> >                 else: return False
> >                 
> >             def __lt__(self, other):
> >                 l1 = len(self.key1)
> >                 l2 = len(other.key1)
> >                 if l1 < l2:
> >                     return True
> >                 elif l1 == l2:
> >                     flag = False
> >                     for i in range(l1):
> >                         if self.key1[i] == other.key1[i]:
> >                             continue
> >                         elif self.key1[i] > other.key1[i]:
> >                             break
> >                         elif self.key1[i] < other.key1[i]:
> >                             flag = True
> >                             break
> >                     return flag
> >                 else:
> >                     return False
> This is the changed code. Now, you can increase the key value of the string type.
> >         def test_size(self):
> >             dict_bst = Dict_bst()
> >             dict_bst.insert(1, 2)
> >             dict_bst.insert("3", 4)
> >             dict_bst.insert(5, None)
> >             self.assertEqual(dict_bst.size(), 3)
> After that, I added a system test.
> >         NodeStrategy = st.builds(Node, st.one_of(st.integers(),st.text(min_size=1)), st.one_of(st.integers(),st.text(min_size=1)))
> >         @given(st.lists(NodeStrategy))
> >         def test_len_size(self, arr):
> >             k = 0
> >             for i in arr:
> >                 arr1 = arr.copy()[k + 1:]
> >                 for j in arr1:
> >                     if i == j:
> >                         arr.remove(j)
> >                 k = k + 1
> >             dict_bst = Dict_bst()
> >             for i in arr:
> >                 dict_bst.insert(i.key, i.value)
> >             self.assertEqual(dict_bst.size(), len(arr))
> 4. Add property-based tests for from_list and to_list, all monoid properties (Associativity, Identity element) for mutable and immutable versions.
 
