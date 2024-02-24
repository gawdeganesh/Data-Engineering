class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


def createLinkedList(list):
    """Creates a linked list from a list of values and returns the head of the list."""
    head = None
    tail = None

    for ele in list:
        new_node = Node(ele)

        if not head:
            head = new_node
            tail = new_node
        else:
            # create a link with new_node's address in the old tail
            tail.next = new_node
            tail = new_node

    return head


def printLinkedList(head):
    current = head

    while current:
        print(current.value, end=" -> ")
        current = current.next

    print("None")


def find_middle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


values = [1, 2, 3, 4, 5]
list_head = createLinkedList(values)


# Print the created linked list
printLinkedList(list_head)

# Example usage
values = [1, 2, 3, 4, 5]
list_head = createLinkedList(values)
middle_node = find_middle(list_head)
print("The middle of the list is:", middle_node.value)

# For an even number of elements
values_even = [1, 2, 3, 4, 5, 6]
list_head_even = createLinkedList(values_even)
middle_node_even = find_middle(list_head_even)
print("The middle of the list is (even number of elements):", middle_node_even.value)
