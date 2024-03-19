class Queue:
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enque(self, value):
        self.items.append(value)

    def deque(self):
        return self.items.pop(0) if not self.isEmpty() else None

    def peek(self):
        return self.items[0]


queue = Queue()

print(queue.isEmpty())

queue.enque(1)
queue.enque(2)
queue.enque(56)

print(queue.peek())

# print(queue.deque())
# print(queue.deque())
