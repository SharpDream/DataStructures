class Node:

  def __init__(self, data=None, next=None) -> None:
    self.data = data
    self.next = next


class SLL:

  def __init__(self) -> None:
    self.head = None

  def insert_at_the_tail(self, data):
    itr = self.head
    node = Node(data)

    if not itr:
      self.head = node
      return

    while itr.next:
      itr = itr.next
    itr.next = node

  def insert_at_the_head(self, data):
    itr = self.head
    node = Node(data)

    self.head = node

    if not itr:
      return

    self.head.next = itr

  def insert(self, index, data):
    itr = self.head

    if not itr or index == 0:
      self.insert_at_the_head(data)
    elif -1 > index > self.get_length():
      return

    count = 0
    while itr is not None:
      if count == index - 1:
        node = Node(data, itr.next)
        itr.next = node

      count += 1
      itr = itr.next

  def pop(self, index):

    itr = self.head

    if not itr:
      return
    elif index == -1:
      index = self.get_length()
    elif index == 0:
      self.head = itr.next
      return
    elif -1 > index > self.get_length():
      return

    count = 0
    while itr is not None:
      if count == index - 1:
        itr.next = itr.next.next
      count += 1
      itr = itr.next

  def remove(self, data):
    itr = self.head
    if not itr:
      return

    count = 0
    while itr is not None:
      if itr.data == data:
        self.pop(count)

      count += 1
      itr = itr.next

  def del_form_head(self):
    self.pop(0)

  def del_for_tail(self):
    self.pop(-1)

  def get_length(self):
    itr = self.head

    if not itr:
      return 0

    count = 0
    while itr.next:
      count += 1
      itr = itr.next
    return count

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
    else:
      return False

  def reverse(self):
    prev, curr = None, self.head

    while curr:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp

    self.head = prev

  def display(self):
    itr = self.head

    if not itr:
      return None
    string = ''
    while itr is not None:
      string += str(itr.data) + "-->" if itr.next else str(itr.data)
      itr = itr.next

    return string
