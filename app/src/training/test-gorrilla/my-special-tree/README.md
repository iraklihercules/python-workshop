# Python data structures & objects test

You are tasked to implement a special tree data structure where the parent node must always be larger in value than all of its children nodes.

The skeleton class **MySpecialTree** is given.
You need to implement the following two functions:

1. `__max_treeify__(self, x)`: this function adds the given value into the tree. Make sure that the parent node is always larger in value than any of its children nodes.
2. `pop_max_value(self)`: this function removes the max value from the tree and return that value. After removing the max value, you might need to call `__max_treeify__` to make sure the tree is still satisfying the requirements that the parent node is larger in value than any of its children nodes.

The `__init__`, `parent`, `left_child` and `right_child` functions are already for you.

The `MySpecialTree` class takes an array of integers and integer `k` representing the number of times your `pop_max_value` function will be called.

Examples:

Input<br>
* values = [1,8,3,0,4,2,9]
* k = 1

Output: [9]

Input
* values = [1,8,3,0,4,2,9]
* k = 3
* Output: [9,8,4]
