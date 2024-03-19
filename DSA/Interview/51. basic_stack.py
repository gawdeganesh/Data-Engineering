class Stack:
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop() if not self.isEmpty() else None

    def peek(self):
        return self.items[-1]


stack = Stack()

print(stack.isEmpty())

stack.push(1)
stack.push(2)
stack.push(56)

print(stack.peek())

print(stack.pop())
print(stack.pop())
