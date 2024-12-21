class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        """Adds a child to the current node."""
        child.parent = self
        self.children.append(child)

    def display(self, prefix=""):
        """Recursively displays the tree structure."""
        print(prefix + ("|- " if prefix else "") + self.data)
        for i, child in enumerate(self.children):
            child.display(prefix +
                          ("|  " if i < len(self.children) - 1 else "   "))


def build_tree():
    """Builds and returns the example tree."""
    root = TreeNode("Electronics")

    laptops = TreeNode("Laptops")
    laptops.add_child(TreeNode("MacBook"))
    laptops.add_child(TreeNode("Microsoft Surface"))
    laptops.add_child(TreeNode("ThinkPad"))

    cell_phones = TreeNode("Cell Phones")
    cell_phones.add_child(TreeNode("iPhone"))
    cell_phones.add_child(TreeNode("Google Pixel"))
    cell_phones.add_child(TreeNode("Vivo"))

    television = TreeNode("Television")
    television.add_child(TreeNode("Samsung"))
    television.add_child(TreeNode("LG"))

    desktop = TreeNode("Desktop")
    desktop.add_child(TreeNode("Gigabyte"))
    desktop.add_child(TreeNode("ASUS"))
    desktop.add_child(TreeNode("NZXT"))
    desktop.add_child(TreeNode("Apple"))

    root.add_child(laptops)
    root.add_child(cell_phones)
    root.add_child(television)
    root.add_child(desktop)

    return root


if __name__ == "__main__":
    tree = build_tree()
    tree.display()
