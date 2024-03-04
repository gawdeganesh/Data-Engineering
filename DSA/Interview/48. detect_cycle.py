class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def detect_cycle_start(head):
    # Step 1: Use Floyd's Cycle Detection algorithm to find if there's a loop
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        # If there's no loop, return None
        return None

    # Step 2: Find the start of the loop
    slow = head  # Reset slow to the start of the list
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # Both pointers now point to the start of the loop


# Helper function to create a linked list and introduce a loop for testing
def create_linked_list_with_loop(values, loop_start_index=None):
    """
    Creates a linked list from the given list of values.
    If loop_start_index is provided and valid, introduces a loop at the specified index.

    :param values: List of values to create nodes.
    :param loop_start_index: Index at which the loop should start. If None, no loop is created.
    :return: The head of the newly created linked list.
    """
    head = None
    tail = None
    loop_start_node = None

    for index, value in enumerate(values):
        new_node = Node(value)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

        if index == loop_start_index:
            loop_start_node = new_node

    # If a valid loop_start_index was provided, point the last node's next to the loop start node
    if loop_start_node:
        tail.next = loop_start_node

    return head


# Example usage
values = [3, 2, 0, -4]
loop_start_index = 1  # Assuming the loop starts at index 1
list_head = create_linked_list_with_loop(values, loop_start_index)
loop_start_node = detect_cycle_start(list_head)
if loop_start_node:
    print(f"Loop starts at node with value: {loop_start_node.value}")
else:
    print("No loop detected.")
