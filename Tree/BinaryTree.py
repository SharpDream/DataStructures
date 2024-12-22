class BinaryTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:

                self.left.addChild(data)
            else:
                self.left = BinaryTree(data)

        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinaryTree(data)

    def find_min(self):
        li = self.in_order_traversal()
        return li[-1]

    def find_max(self):
        li = self.in_order_traversal()
        return li[0]

    def calculate_sum(self):
        sum = 0
        li = self.in_order_traversal()
        for x in li:
            sum += x
        return sum

    def search(self, data):
        if self.data == data:
            return True

        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False

        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def in_order_traversal(self):
        # [left, root, right]
        element = []

        # adding left tree if exist
        if self.left:
            element += self.left.in_order_traversal()

        # adding root
        element.append(self.data)

        # adding right tree if exist
        if self.right:
            element += self.right.in_order_traversal()

        return element

    def post_order_traversal(self):
        # [root, left, right}
        element = []

        # adding root
        element.append(self.data)

        # adding left tree if exist
        if self.left:
            element += self.left.in_order_traversal()

        # adding right tree if exist
        if self.right:
            element += self.right.in_order_traversal()

        return element

    def pre_order_traversal(self):
        # [root, left, right}
        element = []

        # adding left tree if exist
        if self.left:
            element += self.left.in_order_traversal()

        # adding right tree if exist
        if self.right:
            element += self.right.in_order_traversal()

        # adding root
        element.append(self.data)

        return element

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

            # alternate solution
            # max_val = self.left.find_max()
            # self.data = max_val
            # self.left = self.left.delete(max_val)

        return self


def build_tree(li: list):
    root = BinaryTree(li[0])
    for num in li[1:]:
        root.addChild(num)
    return root
