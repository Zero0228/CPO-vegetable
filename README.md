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

> - ### Zhuo Lin: 
> >         Check all functions in the immutable versions.
> >         Add property-based tests for from_list and to_list, all monoid properties (Associativity, Identity element) for immutable versions.
> >         Add filter for immutable.
         
> - ### Liu Fen:
> 
> 2. Fix warnings:
> >     from collections.abc import Iterable
> 
> 4. Add property-based tests for from_list and to_list, all monoid properties (Associativity, Identity element) for mutable and immutable versions.
> >         NodeStrategy = st.builds(Node, st.one_of(st.integers(),st.text(min_size=1)), st.one_of(st.integers(),st.text(min_size=1)))
> >         @given(st.lists(NodeStrategy))
> >         def test_from_list_to_list(self, arr):
> >             k = 0
> >             for i in arr:
> >                 arr1 = arr.copy()[k+1:]
> >                 for j in arr1:
> >                     if i == j:
> >                         arr.remove(j)
> >                 k = k + 1
> >             if len(arr)>2:
> >                 arr = sorted(arr)
> >             dict_bst = Dict_bst().from_list(arr)
> >             tmp_bst = dict_bst.to_list()
> >             if len(arr)>0:
> >                 for i in range(len(arr)):
> >                     self.assertEqual(all(arr[i].key1==tmp_bst[i].key1), True)
> >                     self.assertEqual(arr[i].value, tmp_bst[i].value)
> >                     
> >         @given(st.lists(NodeStrategy))
> >         def test_monoid_identity(self, arr):
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
> >             dict_bst_empty = dict_bst.mempty()
> >             self.assertEqual(dict_bst.mconcat(dict_bst_empty), dict_bst)
> >             self.assertEqual(dict_bst_empty.mconcat(dict_bst), dict_bst)
> >             self.assertEqual(dict_bst.mconcat(dict_bst_empty), dict_bst_empty.mconcat(dict_bst))
> >             
> >         @given(st.lists(NodeStrategy), st.lists(NodeStrategy), st.lists(NodeStrategy))
> >         def test_monoid_associativity(self, arr, arr1, arr2):
> >             k = 0
> >             for i in arr:
> >                 arr0 = arr.copy()[k + 1:]
> >                 for j in arr0:
> >                     if i == j:
> >                         arr.remove(j)
> >                 k = k + 1
> >             dict_bst = Dict_bst()
> >             for i in arr:
> >                 dict_bst.insert(i.key, i.value)
> >             k = 0
> >             for i in arr1:
> >                 arr0 = arr1.copy()[k + 1:]
> >                 for j in arr0:
> >                     if i == j:
> >                         arr1.remove(j)
> >                 k = k + 1
> >             dict_bst1 = Dict_bst()
> >             for i in arr1:
> >                 dict_bst1.insert(i.key, i.value)
> >             k = 0
> >             for i in arr2:
> >                 arr0 = arr2.copy()[k + 1:]
> >                 for j in arr0:
> >                     if i == j:
> >                         arr2.remove(j)
> >                 k = k + 1
> >             dict_bst2 = Dict_bst()
> >             for i in arr2:
> >                 dict_bst2.insert(i.key, i.value)
> >             self.assertEqual(dict_bst.mconcat(dict_bst1).mconcat(dict_bst2), dict_bst.mconcat(dict_bst1.mconcat(dict_bst2)))
>
> 6. Why it is a part of Dict_bst? It should function passed from library user source code. Also for `add` and `square`.
> >   I moved the function to the 'test_mutable.py' file.
>
> 8. Remove key type restriction.
> In this part, I overloaded symbols, such as'>'/'=='/'<'(Node).
> <div align=center><img src="./fig/1.png"/><img src="./fig/3.png"/><img src="./fig/2.png"/></div>
> 
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

 
