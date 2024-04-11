class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class Binary_tree:
    def __init__(self, node) -> None:
        self.head = node


    def print_node(self, node):
        if node.left is not None:
            self.print_node(node.left)
        print(node.data)
        if node.right is not None:
            self.print_node(node.right)


    def print_binary_tree(self):
        self.print_node(self.head)


def main():
    head = Node('Head')
    head.left = Node('Head-Left')
    head.right = Node('Head-Right')
    tree = Binary_tree(head)
    tree.print_binary_tree()


if __name__ == '__main__':
    main()