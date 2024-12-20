class Node:

  def __init__(self, prev=None, data=None, next=None):
    self.prev = prev
    self.data = data
    self.next = next


class DLL:

  def __init__(self):
    self.head = None

  # insertion

  def append(self, data):
    itr = self.head
    if not itr:
      self.head = Node(prev=None, data=data)
      return

    while itr.next:
      itr = itr.next
    itr.next = Node(prev=itr, data=data, next=None)

  def insert_at_beginning(self, data):
    itr = self.head
    if not itr:
      self.head = Node(prev=None, data=data)
      return

    self.head = Node(prev=None, data=data, next=self.head)

  def insert_at(self, index, data):
    itr = self.head

    if index == 0:
      self.insert_at_beginning(data)
      return

    if index == self.get_length():
      self.append(data)
      return

    if index > self.get_length():
      return

    if not itr:
      return

    for _ in range(index - 1):
      itr = itr.next

    new_node = Node(prev=itr, data=data, next=itr.next)

    if itr.next:
      itr.next.prev = new_node
    itr.next = new_node

  # deletation
  def del_at_beginning(self):
    itr = self.head
    if not itr:
      return

    self.head = itr.next

  def del_at_end(self):
    itr = self.head
    if not itr:
      return

    if not itr.next:
      return

    while itr.next.next:
      itr = itr.next
    itr.next = None

  def pop(self, index):
    itr = self.head
    if not itr:
      return

    if index > self.get_length():
      return
    if index == 0:
      self.del_at_beginning()
      return
    if index == self.get_length():
      self.del_at_end()
      return

    count = 0
    while itr is not None:
      if count == index - 1:
        itr.next = itr.next.next
      count += 1
      itr = itr.next

  def get_length(self):
    if not self.head:
      return 0

    itr = self.head
    count = 0
    while itr is not None:
      count += 1
      itr = itr.next

    return count

  def display(self):
    itr = self.head

    if not self.head:
      return

    string = ''
    first = True

    while itr is not None:
      if first:
        string += str(itr.data)
        first = False
      else:
        string += " <--> " + str(itr.data)
      itr = itr.next
    return string

  def search(self, data):
    itr = self.head
    if not itr:
      return

    count = 0
    while itr is not None:
      if itr.data == data:
        return count
      count += 1
      itr = itr.next
    return False

  def reverse(self):
    string = self.display()
    if string is None:
      return

    string = string.split(" <--> ")
    rev_string = ""
    first = True
    for x in range(len(string) - 1, -1, -1):
      if first:
        rev_string += string[x]
        first = False
      else:
        rev_string += " <--> " + string[x]

    return rev_string

  def update(self, prev_data, new_data):
    if not self.head:
      return
    index = self.search(prev_data)
    if index is not False:
      self.pop(index)
      self.insert_at(index, new_data)
      return
