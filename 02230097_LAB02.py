# Definition of a Node in a singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0   # ✅ FIX: renamed

    # Append
    def append(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        print(f"Appended {element} to the list")

    # Get
    def get(self, index):
        if index < 0 or index >= self._size:
            return "Index out of range"
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    # Set
    def set(self, index, element):
        if index < 0 or index >= self._size:
            print("Index out of range")
            return
        
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = element
        print(f"Set element at index {index} to {element}")

    # Size
    def size(self):
        return self._size   # ✅ FIX

    # Prepend
    def prepend(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1
        print(f"Prepend {element} to the list")

    # Print list
    def display(self):
        current = self.head
        print("Print Linked list:[", end="")
        while current:
            print(current.data, end=" ")
            current = current.next
        print("]")


# ------------------ Testing ------------------
X = LinkedList()

X.append(5)

print("Element at index 0:", X.get(0))

X.set(0, 10)

print("Element at index 0:", X.get(0))

print("Current size:", X.size())

X.prepend(10)

X.display()