from collections import deque
# learn more at: https://docs.python.org/3/library/collections.html#collections.deque

stk = deque()
stk.append(1)
stk.append(2)
stk.append(3)

stk.pop()

print(stk)
