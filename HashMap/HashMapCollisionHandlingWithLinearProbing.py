class HashMap:

  def __init__(self):
    self.size = 10
    self.arr = [() for _ in range(1, self.size + 1)]

  def get_hash(self, key):
    sum = 0
    for x in key:
      sum += ord(x)
    return sum % self.size

  def __setitem__(self, key, val):
    index = self.get_hash(key)

    count = 0
    while True:

      if len(self.arr[index]) == 0:
        self.arr[index] = (key, val)
        return

      if self.arr[index][0] == key:
        self.arr[index] = (key, val)
        return

      index += 1
      if index >= self.size:
        index = 0

      if count > self.size:
        return
      count += 1

  def __getitem__(self, key):
    for element in self.arr:
      if len(element) != 0:
        if element[0] == key:
          return element[1]

  def __delitem__(self, key):
    for i, x in enumerate(self.arr):
      if len(x) != 0:
        if x[0] == key:
          del self.arr[i]
          return
