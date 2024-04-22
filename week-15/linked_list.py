class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self, head) -> None:
        self.head = head

    def print_list(self):
        to_print = ''
        element = self.head
        to_print+= (str(element.data) + '-')
        element = element.next
        while element is not None:
            to_print+= (str(element.data) + '-')
            element = element.next
        print(to_print[:-1])