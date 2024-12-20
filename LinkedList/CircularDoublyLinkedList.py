class Node:

  def __init__(self, prev=None, data=None, next=None):
    self.prev = prev
    self.data = data
    self.next = next


class CDLL:

  def __init__(self):
    self.head = None

  def append(self, data):
    if not self.head:
      self.head = Node(data=data)
      self.head.next = self.head
      self.head.prev = self.head
      return

    tail = self.head.prev

    node = Node(prev=tail, data=data, next=self.head)
    tail.next = node
    self.head.prev = node

  def display(self):
    if not self.head:
      print("List is empty.")
      return

    itr = self.head
    nodes = []

    # Traverse the circular list
    while True:
      nodes.append(str(itr.data))
      itr = itr.next
      if itr == self.head:  # Stop when we circle back to the head
        break

    print(" <--> ".join(nodes) + " --> (back to head)")
