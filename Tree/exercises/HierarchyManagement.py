# using Standard Tree


class TreeNode:

    def __init__(self, name, designation):
        self.data = (name, designation)
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, model="both"):

        # print statement
        if model == "both":
            print(f"{self.data[0]} ({self.data[1]})")
            lvl1 = 'f"  |-{self.children[i].data[0]} ({self.children[i].data[1]})"'
            lvl2 = 'f"    |-{child_lvl_2.data[0]} ({child_lvl_2.data[1]})"'
            lvl3 = 'f"      |-{child_lvl_3.data[0]} ({child_lvl_3.data[1]})"'

        elif model == "name":
            print(self.data[0])
            lvl1 = 'f"  |-{self.children[i].data[0]}"'
            lvl2 = 'f"    |-{child_lvl_2.data[0]}"'
            lvl3 = 'f"      |-{child_lvl_3.data[0]}"'

        elif model == "designation":
            print(self.data[1])
            lvl1 = 'f"  |-{self.children[i].data[1]}"'
            lvl2 = 'f"    |-{child_lvl_2.data[1]}"'
            lvl3 = 'f"      |-{child_lvl_3.data[1]}"'

        else:
            print("Invalid Model")
            return

        # lvl: 1
        for i, child_lvl_1 in enumerate(self.children):
            print(eval(lvl1))
            # lvl: 2
            for child_lvl_2 in child_lvl_1.children:
                print(eval(lvl2))
                # lvl: 3
                if len(child_lvl_2.children) >= 1:
                    for child_lvl_3 in child_lvl_2.children:
                        print(eval(lvl3))


def build_management_tree():

    # ceo lvl 0
    root = TreeNode("Nilupul", "CEO")

    # cto lvl 1
    cto = TreeNode("Chinmay", "CTO")

    # cto:under lvl 1:1
    infrastructure_head = TreeNode("Vishwa", "Infrastructure Head")

    # cto:under(infrastructure head):under lvl 1:1:1
    infrastructure_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infrastructure_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto.add_child(infrastructure_head)

    #cto:under lvl 1:1
    cto.add_child(TreeNode("Aamir", "Application head"))

    root.add_child(cto)

    #hr head lvl 1
    hr_head = TreeNode("Gels", "HR Head")

    #hr head:under lvl 1:1
    hr_head.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    root.add_child(hr_head)

    return root


if __name__ == '__main__':
    root_node = build_management_tree()
    print("\n")
    root_node.print_tree("name")
    print("\n")
    root_node.print_tree("designation")
    print("\n")
    root_node.print_tree("both")
