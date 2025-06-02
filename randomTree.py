import random

# Node class to store coordinates, level, parent, and label
class Node:
    def __init__(self, x, y, level, label="Root", parent=None):
        self.x = x
        self.y = y
        self.level = level
        self.label = label
        self.parent = parent

# Recursive tree generator
def generate_tree(x, y, level, label="Root", parent=None):
    if level > 4:  # Limit depth
        return

    node = Node(x, y, level, label, parent)

    # Create indentation based on level
    indent = "    " * (level - 1)
    print(f"{indent}--- [{label}] ({x}, {y})")

    # Determine number of children (1 to 3)
    num_children = random.randint(1, 3)

    # Possible labeled directions
    directions = {
        "Left": (x - 1, y + random.randint(1, 2)),
        "Center": (x, y + random.randint(1, 2)),
        "Right": (x + 1, y + random.randint(1, 2))
    }

    # Randomly pick branches to grow
    selected_directions = random.sample(list(directions.items()), k=num_children)

    for direction_label, (new_x, new_y) in selected_directions:
        generate_tree(new_x, new_y, level + 1, direction_label, node)

# Start the tree
generate_tree(0, 0, 1)
