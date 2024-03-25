class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        Pushes an element onto the stack and updates the min_stack accordingly.
        """

        self.stack.append(x)

        if not self.min_stack or self.min_stack[-1] > x:
            self.min_stack.append(x)

    def top(self):
        """
        Gets the top element of the stack.
        """
        if not self.min_stack:
            return self.min_stack[-1]

    def pop(self):
        """
        Removes the element on top of the stack and updates the min_stack accordingly.
        """

        if self.stack:
            top = self.stack.pop()

        if top == self.min_stack[-1]:
            self.min_stack.pop()

    def getMin(self):
        """
        Retrieves the minimum element in the stack.
        """
        if self.min_stack:
            return self.min_stack[-1]


# Example usage:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Returns -3
minStack.pop()
print(minStack.top())  # Returns 0
print(minStack.getMin())  # Returns -2
