# Step 1: Define the Node class
class Node:
    def __init__(root, value):
        root.value = value
        root.left = None
        root.right = None

# Step 2: Define BST insertion function
def insert_bst(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root

# Step 3: Define traversal functions
def print_preorder(node):
    if node is None:
        return
    print(node.value, end=" ")
    print_preorder(node.left)
    print_preorder(node.right)

def print_inorder(node):
    if node is None:
        return
    print_inorder(node.left)
    print(node.value, end=" ")
    print_inorder(node.right)

def print_postorder(node):
    if node is None:
        return
    print_postorder(node.left)
    print_postorder(node.right)
    print(node.value, end=" ")

# Step 4: Insert 7 values
values = [8, 3, 10, 1, 6, 14, 4 , 15 ,100 ,2 ,35]  # Example values
root = None
for val in values:
    root = insert_bst(root, val)

# Step 5: Print tree in different traversals
print("Preorder traversal:")
print_preorder(root)
print("\nInorder traversal:")
print_inorder(root)
print("\nPostorder traversal:")
print_postorder(root)
