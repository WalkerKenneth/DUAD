class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None


class Queue:
    def __init__(self, node) -> None:
        self.head = node
        self.tail = node


    def push_left(self, node):
        self.head.previous = node
        node.next = self.head
        self.head = node


    def push_right(self, node):
        self.tail.next = node
        node.previous = self.tail
        self.tail = node


    def pop_left(self):
        value = self.head
        self.head = self.head.next
        self.head.next = None
        return value


    def pop_right(self):
        value = self.tail
        self.tail = self.tail.previous
        self.tail.next = None
        return value


    def print_queue(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


def main():
    node = Node(5)
    numbers = Queue(node)
    for count in range(4,0, -1):
        numbers.push_left(Node(count))
    for count in range(6, 11):
        numbers.push_right(Node(count))
    numbers.print_queue()


if __name__ == '__main__':
    main()