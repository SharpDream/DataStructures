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


  def in_order_traversal(self):
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

def build_tree(li: list):
  root = BinaryTree(li[0])
  for num in li[1:]:
      root.addChild(num)
  return root
