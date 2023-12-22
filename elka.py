def print_pyramid_tree(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))

# Höhe der Pyramide festlegen
tree_height = 7

# Weihnachtsbaum in Pyramidenform ausgeben
print_pyramid_tree(tree_height)
