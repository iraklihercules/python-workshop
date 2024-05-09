# Python (coding): Entry-Level Algorithms

**Instructions**

You are given:
* **n** : the size of the array
* **val1** : an integer
* **arr** : an array of integers
Write a function that takes the array **arr**, its size **n**, and the integer **val1** as input and return an array containing the count of integers that are smaller than, equal to, and greater than **val1**, respectively.

**Example:**

Input:
* **n** = 5
* **val1** = 6
* **arr** = 2 4 6 8 10

Output:
* 2 1 2

Explanation
* In the given example, there are two integers smaller than 6 (2 and 4), one integer equal to 6, and two integers greater tham 6 (8 and 10).


```python
def countIntegers(n, val, arr):
	smaller = sum(1 for num in arr if num < val)
	equal = sum(1 for num in arr if num == val)
	greater = sum(1 for num in arr if num > val)
	return [smaller, equal, greater]

n = int(input())
val = int(input())
arr = list(map(int, input().split()))

result = countIntegers(n, val, arr)
print(' '.join(map(str, result)))
```

```
-- Test 1
  -- Input:
    1
    1
    2
  -- Output:
    0 0 1

-- Test 2
  -- Input:
    7
    8
    10 4 6 2 12 8 9
  -- Output:
    3 1 3

-- Test 3
  -- Input:
    5
    6
    2 4 6 8 10
  -- Output:
    2 1 2
```
