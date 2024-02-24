class Node:
    def __init__(self, value: int = None) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None  # define empty Linked list

    def append(self, value: int) -> None:
        new_node = Node(value)

        if not self.head:  # if its the first value or node make it a head
            self.head = new_node

        else:  # iterate the nodes and append the new node
            current_node = self.head

            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node

    def print_list(self):
        current_node = self.head

        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next

        print("None")

    def reverse(self):
        # initialize three pointers
        prev = None
        current = self.head
        next_node = current.next

        while current:
            next_node = current.next  # Save the next node

            # shift the direction of the nodes
            current.next = prev

            # shift the nodes
            prev = current
            current = next_node

        # current pointer is at null and the previous pointer is the head

        self.head = prev


# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

print("Original list:")
ll.print_list()

ll.reverse()

print("Reversed list:")
ll.print_list()
