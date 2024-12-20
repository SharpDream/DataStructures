from collections import deque
# learn more at: https://docs.python.org/3/library/collections.html#collections.deque

queue = deque()
queue.appendleft(1)
queue.appendleft(2)
queue.appendleft(3)

queue.pop()

print(queue)
