# Funktion zum Drucken eines Baumzweigs
def print_branch(branch_length, spaces):
    if branch_length > 5:
        print(" " * spaces + "*" * branch_length)
        print_branch(branch_length - 2, spaces + 1)
        print_branch(branch_length - 2, spaces - 1)

# Funktion zum Drucken des Weihnachtsbaums
def print_tree(height):
    print_branch(height * 2, height)

# Höhe des Baumes festlegen
tree_height = 5

# Baum in Textform ausgeben
print_tree(tree_height)
