

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if not self.value:
            self.value = value
            return

        if value < self.value:
            if self.left:
                print(value, "left insert")
                self.left.insert(value)
            else:
                print(value, "left new")
                self.left = Node(value)
        elif value > self.value:
            if self.right:
                print(value, "right insert")
                self.right.insert(value)
            else:
                print(value, "right new")
                self.right = Node(value)
        else:
            print(value, "skip")

    def print_tree(self):
        return self._traversal_inorder(self, [])

    def _traversal_inorder(self, node, data):
        if node:
            data.append(node.value)
            self._traversal_inorder(node.left, data)
            self._traversal_inorder(node.right, data)
        return data


if __name__ == "__main__":

    tree = Node(15)
    data = [12, 4, 1, 4, 5, 69, 678, 3, 2, 46, 7, 3, 6, 62, 14, 6]
    print("input", data)

    for x in data:
        tree.insert(x)

    print(tree.print_tree())


