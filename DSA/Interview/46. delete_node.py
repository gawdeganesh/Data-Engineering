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


def delete_node(head, index):

    count = 0
    current = head

    if index == 0:
        head = current.next
        return head

    while current:
        if count == index - 1:  # Find the node just before the index
            if current.next:
                current.next = current.next.next  # Bypass the node at index
            break  # Node found and deleted; exit the loop
        else:
            current = current.next
            count += 1

    return head


values = [25, 453, 12, -1, 34]
list_head = createLinkedList(values)


# Print the created linked list
printLinkedList(list_head)

# delete the node at index
new_head = delete_node(list_head, 0)
printLinkedList(new_head)


new_head = delete_node(list_head, 4)
printLinkedList(new_head)
