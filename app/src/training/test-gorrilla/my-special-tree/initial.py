def special_tree(values, k):
    # DO NOT MODIFY THE CODE BELOW
    my_tree = MySpecialTree(values)
    soln = []
    for val in range(k):
        soln.append(my_tree.pop_max_value())

    return soln
    # DO NOT MODIFY THE CODE ABOVE


class MySpecialTree:
    def __init__(self, values=None):
        self.data = values or []
        for x in range(len(values) // 2, -1, -1):
            self.__max_treeify__(x)

    def parent(self, x):
        return x >> 1

    def left_child(self, x):
        return (x << 1) + 1

    def right_child(self, x):
        return (x << 1) + 2

    def __max_treeify__(self, x):
        pass

    def pop_max_value(self):
        pass


data = [
    {"k": 1, "values": [1, 8, 3, 0, 4, 2, 9], "expected": [9]},
    {"k": 3, "values": [1, 8, 3, 0, 4, 2, 9], "expected": [9, 8, 4]},
    {"k": 2, "values": [8, 8, 8, 8, 8, 8, 8, 8], "expected": [8, 8]},
    {"k": 5, "values": [9, 9, 3, 1, 4, 5, 9, 2, 5], "expected": [9, 9, 9, 5, 5]},
]
for row in data:
    result = special_tree(row["values"], row["k"])
    print(row["expected"], result)
