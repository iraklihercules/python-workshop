
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, value):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(value)

    def length(self):
        curr = self.head
        total = 0
        while curr.next is not None:
            total += 1
            curr = curr.next
        return total

    def print_list(self):
        curr = self.head
        data = []
        while curr.next is not None:
            curr = curr.next
            data.append(curr.value)
        return data


if __name__ == "__main__":
    my_list = LinkedList()
    for x in [2, 56, 71,8, 14, 77, 5]:
        my_list.append(x)
    print("length", my_list.length())
    print("list", my_list.print_list())
