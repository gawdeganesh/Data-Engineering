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
    current_node = head

    while current_node:
        print(current_node.value, end=" -> ")
        current_node = current_node.next

    print("None")


def merge_linked_list(list1, list2):

    # create a dummy head to store a sorted list

    dummy_node = Node(0)  # head element is 0 for merged list
    tail = dummy_node

    while list1 and list2:

        if list1.value == list2.value:
            tail.next = list1
            list1 = list1.next
            list2 = list2.next

        elif list1.value < list2.value:
            tail.next = list1
            list1 = list1.next

        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    # At least one of l1 and l2 can still have elements left; attach the remainder

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    # because head has the value of 0 so populate the linked list from the next position

    return dummy_node.next


list1 = [1, 2, 3, 4, 5, 6, 7, 10]
list2 = [-1, 0, 1, 11, 12, 13]

linkedlist_1 = createLinkedList(list1)
linkedlist_2 = createLinkedList(list2)

printLinkedList(createLinkedList(list1))
printLinkedList(createLinkedList(list2))


print("Merged sorted list:")
printLinkedList(merge_linked_list(linkedlist_1, linkedlist_2))
