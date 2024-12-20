# Collision Handling In Hash Table with channing


class HashMap:

  def __init__(self):
    self.size = 10
    self.arr = [[] for _ in range(1, self.size + 1)]

  def get_hash(self, key):
    sum = 0
    for x in key:
      sum += ord(x)
    return sum % self.size

  def __setitem__(self, key, val):
    index = self.get_hash(key)

    for i, element in enumerate(self.arr[index]):
      if element[0] == key:
        self.arr[index][i] = (key, val)
        return
    self.arr[index].append((key, val))

  def __getitem__(self, key):
    index = self.get_hash(key)
    for element in self.arr[index]:
      if element[0] == key:
        return element[1]

  def __delitem__(self, key):
    index = self.get_hash(key)

    if len(self.arr[index]) == 0:
      return

    for i, element in enumerate(self.arr[index]):
      if element[0] == key:
        del self.arr[index][i]
        return
