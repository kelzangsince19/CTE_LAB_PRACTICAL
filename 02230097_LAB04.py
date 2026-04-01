#part 1 (task1 and task2)
class ArrayQueue:
    def __init__(self, capacity=10):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.count = 0

        print("Created new Queue with capacity:", capacity)

    def is_empty(self):
        return self.count == 0

    # 1. Enqueue
    def enqueue(self, element):
        if self.count == self.capacity:
            print("Queue Overflow")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = element
        self.count += 1
        print(f"Enqueued {element} to the queue")

    # 2. Dequeue
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        element = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        print(f"Dequeued element: {element}")
        return element

    # 3. Peek
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    # 4. Size
    def size(self):
        return self.count

    # 5. Display
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        items = []
        for i in range(self.count):
            index = (self.front + i) % self.capacity
            items.append(self.queue[index])
        print("Display queue:", items)


q = ArrayQueue()

q.enqueue(10)
q.display()
q.enqueue(20)
q.display()
q.enqueue(30)
q.display()
print("Front element:", q.peek())
q.dequeue()
q.display()
print("Queue size:", q.size())

#part2. LinkedQueue class
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedQueue class
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
        print("Created new LinkedQueue")

    # 4. is_empty
    def is_empty(self):
        return self.front is None

    # 1. enqueue
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:  # Queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.count += 1
        print(f"Enqueued {element} to the queue")

    # 2. dequeue
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        removed = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.count -= 1
        print(f"Dequeued element: {removed}")
        return removed

    # 3. peek
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.data

    # 5. size
    def size(self):
        return self.count

    # 6. display
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("null")



lq = LinkedQueue()
lq.enqueue(10)
lq.display()
lq.enqueue(20)
lq.display()
lq.enqueue(30)
lq.display()
print("Front element:", lq.peek())
lq.dequeue()
lq.display()
print("Queue size:", lq.size())
