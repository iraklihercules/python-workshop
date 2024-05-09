# https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if not self.left:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if not self.right:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, value):
        if self.data == value:
            return self

        if self.left and self.data > value:
            return self.left.search(value)

        if self.right:
            return self.right.search(value)

        return None

    def print_tree(self):
        return self._preorder_recursively(self, [])

    def _preorder_recursively(self, current_node, data):
        if current_node:
            data.append(current_node.data)
            data = self._preorder_recursively(current_node.left, data)
            data = self._preorder_recursively(current_node.right, data)
        return data


root = Node(12)
root.insert(5)
root.insert(17)
root.insert(30)
root.insert(9)
root.insert(1)

print(root.print_tree())
# [12, 5, 1, 9, 17, 30]

print(root.search(9).data)
# 9
