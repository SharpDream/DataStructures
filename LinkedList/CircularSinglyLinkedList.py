class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class CSLL:

  def __init__(self):
    self.head = None

  def append(self, data):
    if not self.head:
      self.head = Node(data)
      self.head.next = self.head
      return

    itr = self.head
    while itr.next != self.head:
      itr = itr.next

    node = Node(data)
    itr.next = node
    node.next = self.head

  def display(self):
    if not self.head:
      print(None)
      return

    nodes = []
    itr = self.head
    while True:
      nodes.append(str(itr.data))
      itr = itr.next
      if itr == self.head:
        break
    print(" --> ".join(nodes) + " --> (back to head)")

  def remove(self, data):
    if not self.head:
      return

    itr = self.head

    if data == itr.data:
      if self.head == itr.next:
        self.head = None

      else:
        while itr.next != self.head:
          itr = itr.next

        itr.next = itr.next.next
        self.head = itr.next
      return

    while itr.next != self.head:
      if itr.next.data == data:
        itr.next = itr.next.next
        return
      itr = itr.next
