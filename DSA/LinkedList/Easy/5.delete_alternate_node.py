class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_alternate_nodes(self):
        if not self.head:
            return

        current = self.head

        while current and current.next:
            current.next = current.next.next
            current = current.next

    def display(self):
       curr = self.head
       result = ''
       while curr!= None:
            result = result + str(curr.data) + '->'
            curr = curr.next 
       return  print(result[:-2])  

# Example usage:
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append()

print("Original Linked List:")
llist.display()

llist.delete_alternate_nodes()

print("Linked List after deleting alternate nodes:")
llist.display()
