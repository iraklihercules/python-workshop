

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        if self.value:
            if self.next:
                self.next.add(value)
            else:
                self.next = Node(value)
        else:
            self.value = value

    def insert(self, value, index):
        pointer = self
        for x in range(index - 1):
            pointer = pointer.next

        new_node = Node(value)
        new_node.next = pointer.next
        pointer.next = new_node

    def delete(self, index):
        pointer = self
        for x in range(index - 1):
            pointer = pointer.next
        element = pointer.next
        pointer.next = element.next
        del element

    def print_list(self):
        return self._traverse(self, [])

    def _traverse(self, node, data):
        if node:
            data.append(node.value)
            self._traverse(node.next, data)
        return data


if __name__ == "__main__":
    my_list = Node("A")

    for x in ["B", "C", "D", "E"]:
        my_list.add(x)
    print(my_list.print_list())

    my_list.insert("X", 2)
    print(my_list.print_list())

    my_list.delete(3)
    print(my_list.print_list())
