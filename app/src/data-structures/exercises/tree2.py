

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:

            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            elif data > self.data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)

        else:
            self.data = data

    def print_tree(self):
        return self._traversal(self, [])

    def _traversal(self, node, data):
        if node:
            self._traversal(node.left, data)
            data.append(node.data)
            self._traversal(node.right, data)
        return data


if __name__ == "__main__":
    data = [5, 7, 19, 12, 99, 100, 55, 45, 1, 4, 6, 9, 44, 23]

    tree = Node(75)
    for x in data:
        tree.insert(x)

    print(tree.print_tree())
