def count_integers(n, val, arr):
    smaller = sum(1 for num in arr if num < val)
    equal = sum(1 for num in arr if num == val)
    greater = sum(1 for num in arr if num > val)
    return [smaller, equal, greater]


data = [
    [1, 1, [2]],
    [7, 8, [10, 4, 6, 2, 12, 8, 9]],
    [5, 6, [2, 4, 6, 8, 10]],
]

for row in data:
    n, val, arr = row
    result = count_integers(n, val, arr)
    print(" ".join(map(str, result)))
