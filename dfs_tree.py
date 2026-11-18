class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Pre-order Traversal: Root -> Left -> Right
def print_preorder(node):
    if node:
        print(node.val, end=", ")
        print_preorder(node.left)
        print_preorder(node.right)


# In-order Traversal: Left -> Root -> Right
def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.val, end=", ")
        print_inorder(node.right)


# Post-order Traversal: Left -> Right -> Root
def print_postorder(node):
    if node:
        print_postorder(node.left)
        print_postorder(node.right)
        print(node.val, end=", ")


if __name__ == "__main__":
    print("==========================================")
    print("Assessment 3.6: DFS Method in Tree")
    print("Name: Villarino, Daniel | BSIT - 2C")
    print("==========================================\n")

    # Constructing the binary tree based on Assessment 3.5 diagram
    root = Node('D')

    # Level 1
    root.left = Node('A')
    root.right = Node('N')

    # Level 2
    root.left.left = Node('I')
    root.left.right = Node('E')
    root.right.left = Node('L')
    root.right.right = Node('V')

    # Level 3 (Leaves/Sub-leaves)
    root.left.left.left = Node('I')
    root.left.left.right = Node('L')

    root.left.right.left = Node('L')
    root.left.right.right = Node('A')

    root.right.left.left = Node('R')
    root.right.left.right = Node('I')

    root.right.right.left = Node('N')
    root.right.right.right = Node('O')

    print("PREORDER:")
    print_preorder(root)
    print("\n")

    print("INORDER:")
    print_inorder(root)
    print("\n")

    print("POSTORDER:")
    print_postorder(root)
    print("\n")