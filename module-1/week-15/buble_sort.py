from linked_list import Node, Linked_list

def bubble_sort(list_to_sort):
    for i in range(0, len(list_to_sort)):
        changes = False
        for y in range(len(list_to_sort) - 1, i, -1):
            current_element = list_to_sort[y]
            next_element = list_to_sort[y - 1]
            if current_element < next_element:
                list_to_sort[y] = next_element
                list_to_sort[y - 1] = current_element
                changes = True
        if not changes:
            return


def bubble_sort_linked_list(head):
    if not head or not head.next:
        return head
    
    sorted = False
    while not sorted:
        sorted = True
        prev = None
        current = head
        while current.next:
            if current.data > current.next.data:
                if prev:
                    prev.next = current.next
                else:
                    head = current.next
                temp = current.next.next
                current.next.next = current
                current.next = temp
                prev = current.next
                sorted = False
            else:
                prev = current
                current = current.next

    return head

def main():
    head = Node(5)
    head.next = Node(1)
    head.next.next = Node(11)
    head.next.next.next = Node(3)

    unordered_list = Linked_list(head)
    unordered_list.print_list()

    ordered_list = Linked_list(bubble_sort_linked_list(unordered_list.head))
    ordered_list.print_list()


if'__main__' == __name__:
    main()