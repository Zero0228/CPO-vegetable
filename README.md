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

## Updat
> - **Zhuo Lin**: Check all functions in the immutable versions.
>                 Add property-based tests for from_list and to_list, all monoid properties (Associativity, Identity element) for immutable versions.
>                 Add filter for immutable.
> - **Liu Fen**: 
 
