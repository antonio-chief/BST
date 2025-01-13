class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Binary search function
def search(node, target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)

# Helper function to insert values into the BST
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# Build the BST with hardcoded values
root = None
values = [15, 10, 20, 8, 12, 17, 25]
for value in values:
    root = insert(root, value)

# Hardcoded target value
target = 12

# Search for the target value in the BST
result = search(root, target)

# Print the result
if result is not None:
    print(f"Found node with value: {result.data}")
else:
    print(f"Value {target} not found in the tree.")
