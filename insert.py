class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(node, data):
    if node is None:  # Base case: Create a new node if the current node is None
        return TreeNode(data)
    else:
        if data < node.data:  # If data is smaller, insert into the left subtree
            node.left = insert(node.left, data)
        elif data > node.data:  # If data is larger, insert into the right subtree
            node.right = insert(node.right, data)
    return node  # Return the (updated) current node


# Example usage
if __name__ == "__main__":
    root = None  # Start with an empty tree
    values = [10, 5, 15, 7]  # Values to insert into the tree
    for value in values:
        root = insert(root, value)

    # Function to print the tree (Inorder Traversal)
    def inorder_traversal(node):
        if node is not None:
            inorder_traversal(node.left)
            print(node.data, end=" ")
            inorder_traversal(node.right)

    # Display the tree
    print("Inorder Traversal of the Tree:")
    inorder_traversal(root)