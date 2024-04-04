class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self, node) -> None:
        self.first_element = node


    def push(self, node):
        node.next = self.first_element
        self.first_element = node


    def pop(self):
        value = self.first_element
        self.first_element = self.first_element.next
        return value


    def print_stack(self):
        node = self.first_element
        while node is not None:
            print(node.data)
            node = node.next


def main():
    node = Node(1)
    stack = Stack(node)
    for count in range(2, 11):
        stack.push(Node(count))
    stack.print_stack()
    print('----------------')
    for count in range(0, 5):
        stack.pop()
    stack.print_stack()


if __name__ == '__main__':
    main()