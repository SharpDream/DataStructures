# Using Standard Tree

class TreeNode:
  def __init__(self, data):
      self.data = data
      self.child = []
      self.parent = None

  def addChild(self, children):
      self.parent = None
      self.child.append(children)

  def display(self, model=3):
      print(self.data)

      if model == 1:
          one = 'f"  |-{lvl_1.data}"'
          two = ""
          three = ""
          end_val_one = "\n"
          end_val_two = ""
          end_val_three = ""
      elif model == 2:
          two = 'f"    |-{lvl_2.data}"'
          one = 'f"  |-{lvl_1.data}"'
          three = ''
          end_val_one = "\n"
          end_val_two = "\n"
          end_val_three = ""
      elif model == 3:
          three = 'f"      |-{lvl_3.data}"'
          two = 'f"    |-{lvl_2.data}"'
          one = 'f"  |-{lvl_1.data}"'
          end_val_one = "\n"
          end_val_two = "\n"
          end_val_three = "\n"
      else:
          print("Invalid Model")
          return

      for lvl_1 in self.child:
          print(eval(one) if one != '' else '', end=end_val_one)
          for lvl_2 in lvl_1.child:
              print(eval(two) if two != '' else '', end=end_val_two)
              for lvl_3 in lvl_2.child:
                  print(eval(three) if three != '' else '', end=end_val_three)


def LocationTree():
  root = TreeNode("Global")

  india = TreeNode("India")

  gujarat = TreeNode("gujarat")
  gujarat.addChild(TreeNode("Ahmedabad"))
  gujarat.addChild(TreeNode("Baroda"))

  karnataka = TreeNode("Karnataka")
  karnataka.addChild(TreeNode("Bangluru"))
  karnataka.addChild(TreeNode("Mysore"))

  india.addChild(gujarat)
  india.addChild(karnataka)


  usa = TreeNode("usa")

  new_jersey = TreeNode("New Jersey")
  new_jersey.addChild(TreeNode("Princeton"))
  new_jersey.addChild(TreeNode("Trenton"))

  california = TreeNode("California")
  california.addChild(TreeNode("San Francisco"))
  california.addChild(TreeNode("Mountain View"))
  california.addChild(TreeNode("Palo Alto"))

  usa.addChild(new_jersey)
  usa.addChild(california)

  root.addChild(india)
  root.addChild(usa)

  return root




if __name__ == '__main__':
  root_node = LocationTree()
  root_node.display(1)

  root_node.display(2)
  root_node.display(3)