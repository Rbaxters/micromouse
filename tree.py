class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

# Function to find the height of the tree
def find_height(root):
    if not root:
        return -1
    if not root.children:
        return 0
    return 1 + max(find_height(child) for child in root.children)

# Helper function to place nodes in a 2D array using preorder traversal
def preorder(root, row, col, ans, spacing):
    if not root:
        return

    ans[row][col] = str(root.data)

    num = len(root.children)
    if num == 0:
        return

    # Total width to spread children horizontally
    total_width = spacing * (num - 1)

    # Start column for first child
    start_col = col - total_width // 2

    for i, child in enumerate(root.children):
        child_col = start_col + i * spacing
        preorder(child, row + 1, child_col, ans, spacing // 2)

# Function to convert the tree to a 2D matrix
def tree_to_matrix(root):
    height = find_height(root)
    rows = height + 1
    cols = 2 ** (height + 3)  # more space for wide trees

    ans = [["" for _ in range(cols)] for _ in range(rows)]

    preorder(root, 0, cols // 2, ans, spacing=cols // 4)

    return ans

# Function to print the 2D matrix
def print_2d_array(arr):
    for row in arr:
        print("".join(cell if cell else " " for cell in row))

if __name__ == "__main__":
    # Sample N-ary tree:
    #         1
    #      /  |  \
    #     2   3   4
    #        / \
    #       5   6
    root = Node(1)
    root.children = [Node(2), Node(3), Node(4)]
    root.children[1].children = [Node(5), Node(6)]
    root.children[2].children = [Node(7), Node(9)]
    root.children[0].children = [Node(8), Node(10)]
    root.children[0].children[0].children = [Node(11), Node(12)]
    
    result = tree_to_matrix(root)
    print_2d_array(result)
