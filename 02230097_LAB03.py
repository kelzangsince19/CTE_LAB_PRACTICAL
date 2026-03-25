# Task 1: ArrayStack Class Structure

class ArrayStack:
    def __init__(self, capacity=10):
        # Private array to store elements
        self.__stack = [None] * capacity
        # Variable to track the top of the stack
        self.__top = -1
        self.__capacity = capacity
        print(f"Created new ArrayStack with capacity: {capacity}")

    #Task 2: Implement Array-based Stack Operations
    def is_empty(self):
        # Check if stack is empty
        return self.__top == -1
    def push(self, element):
        if self.__top >= self.__capacity - 1:
            print("Stack Overflow! Cannot push element.")
            return
        self.__top += 1
        self.__stack[self.__top] = element
        print(f"Pushed {element} to the stack")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop element.")
            return None
        popped = self.__stack[self.__top]
        self.__stack[self.__top] = None
        self.__top -= 1
        print(f"Popped element: {popped}")
        return popped

    def peek(self):
        if self.is_empty():
            print("Stack is empty! No top element.")
            return None
        return self.__stack[self.__top]

    def is_empty(self):
        return self.__top == -1

    def size(self):
        return self.__top + 1

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Display stack:", self.__stack[:self.__top + 1])

# Example usage
if __name__ == "__main__":
    stack = ArrayStack()
    print("Stack is empty:", stack.is_empty())

    stack.push(10)
    stack.display()

    stack.push(20)
    stack.display()

    stack.push(30)
    stack.display()

    print("Top element:", stack.peek())

    stack.pop()
    print("Stack size:", stack.size())
    stack.display()

#Part 2: Stack Implementation using Linked List
# Task 3: Linked List Stack Class Structure
# Node class to store data and next reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedStack class
class LinkedStack:
    def __init__(self):
        self.top = None  # Reference to top node (head of linked list)
        self.count = 0   # Size counter
        print("Created new LinkedStack")
#Task 4
    def is_empty(self):
        # Check if stack is empty
        return self.top is None
    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
        print(f"Pushed {element} to the stack")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop element.")
            return None
        popped = self.top.data
        self.top = self.top.next
        self.count -= 1
        print(f"Popped element: {popped}")
        return popped

    def peek(self):
        if self.is_empty():
            print("Stack is empty! No top element.")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Display stack:", " -> ".join(elements) + " -> null")

# Example usage
if __name__ == "__main__":
    linked_stack = LinkedStack()
    print("Stack is empty:", linked_stack.is_empty())

    linked_stack.push(10)
    linked_stack.display()

    linked_stack.push(20)
    linked_stack.display()

    linked_stack.push(30)
    linked_stack.display()

    print("Top element:", linked_stack.peek())

    linked_stack.pop()
    linked_stack.display()

    print("Stack size:", linked_stack.size())
