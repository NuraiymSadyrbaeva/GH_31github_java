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
#testing
print("Frohe Weihnachten!")
print("Genieße die festliche Zeit!")


weihnachtslieder = [
    "Stille Nacht",
    "O Tannenbaum",
    "Jingle Bells",
    "O du fröhliche",
    "Rudolph the Red-Nosed Reindeer",
    "Feliz Navidad"
]

print("Hier sind einige beliebte Weihnachtslieder:")
for lied in weihnachtslieder:
    print(lied)
#gonew
