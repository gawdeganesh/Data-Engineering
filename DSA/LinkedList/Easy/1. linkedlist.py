class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:

        # Empty linked list
        self.head = None
        # no of nodes
        self.n = 0

    def __len__(self):
        return self.n

    def insert_head(self, value):

        # new node
        new_node = Node(value)

        # create connection
        new_node.next = self.head

        # reassign head
        self.head = new_node

        # increment n
        self.n = self.n + 1

    def __str__(self):
        curr = self.head

        result = ""

        while curr != None:
            result = result + str(curr.data) + "->"
            curr = curr.next
        return result[:-2]

    def insert_head(self, value):
        new_node = Node(value)

        new_node.next = self.head

        self.head = new_node
        self.n = self.n + 1

    def append(self, value):
        new_node = Node(value)

        # if the list is empty
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return

        curr = self.head

        while curr.next != None:
            curr = curr.next

        # you are at the last node, assign new node 's address to last node
        curr.next = new_node
        self.n = self.n + 1
        return

    def insert_after(self, after, value):
        new_node = Node(value)

        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

            # case 1 : you found the item after break
            # case 2 : loop completed and after item is not found

        if curr == None:
            return "Item not found"
        else:
            # break the connection : store the next value's address in the new node and current node should point to new node
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1

    def printMiddle(self):
        counter = 0
        curr = self.head

        if self.n != 0:
            while curr != None:
                if self.n // 2 == counter:
                    return print(f"the middle of the linked list is {curr.data}")
                else:
                    curr = curr.next
                    counter += 1
        else:
            return print("Empty list")


L = LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)

print(L)

L.insert_head(32)
L.append(23)
L.insert_after(32, 20)
print(L)
print(len(L))

L.printMiddle()
