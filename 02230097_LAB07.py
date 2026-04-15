# Node Class
class Node:
    def __init__(self, value):
        self.value = value   # Value of the node
        self.left = None     # Reference to left child
        self.right = None    # Reference to right child


# Binary Tree Class
class BinaryTree:
    def __init__(self, root=None):
        self.root = root     # Reference to root node
# Create an empty tree
tree = BinaryTree()

# Print the root
print("Created new Binary Tree")
print("Root:", tree.root)

###task2
# Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Binary Tree Class
class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        print("Created new Binary Tree")
        print("Root:", self.root)

    # 1. Height of tree
    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    # 2. Size of tree (total nodes)
    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    # 3. Count leaf nodes
    def count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    # 4. Check Full Binary Tree
    def is_full_binary_tree(self, node):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left and node.right:
            return (self.is_full_binary_tree(node.left) and
                    self.is_full_binary_tree(node.right))
        return False

    # 5. Check Complete Binary Tree
    def is_complete_binary_tree(self):
        if self.root is None:
            return True

        queue = [self.root]
        flag = False

        while queue:
            current = queue.pop(0)

            if current.left:
                if flag:
                    return False
                queue.append(current.left)
            else:
                flag = True

            if current.right:
                if flag:
                    return False
                queue.append(current.right)
            else:
                flag = True

        return True
    
# Example Tree Creation
# Creating nodes manually
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Create Binary Tree
tree = BinaryTree(root)

# Output
print("\nTree Height:", tree.height(tree.root))
print("Total Nodes:", tree.size(tree.root))
print("Leaf Nodes Count:", tree.count_leaves(tree.root))
print("Is Full Binary Tree:", tree.is_full_binary_tree(tree.root))
print("Is Complete Binary Tree:", tree.is_complete_binary_tree())